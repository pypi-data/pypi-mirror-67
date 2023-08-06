from __future__ import annotations

from functools import partial
from functools import wraps
from itertools import chain
from multiprocessing import cpu_count
from pathlib import Path
from tempfile import gettempdir
from tempfile import TemporaryDirectory
from typing import Any
from typing import Callable
from typing import Optional
from typing import TypeVar
from typing import Union

import joblib
from atomic_write_path import atomic_write_path
from functional_itertools import CDict
from functional_itertools import CList
from joblib import delayed
from joblib import Parallel
from numpy import array
from numpy import memmap
from numpy import nan
from numpy import ndarray

from joblib_windower.errors import InvalidWindowError


CPU_COUNT = cpu_count()
TEMP_DIR = gettempdir()
T = TypeVar("T")


def _writes_output(func: Callable[..., Any]) -> Callable[..., None]:
    @wraps(func)
    def wrapped(*args: Any, _output: ndarray, _index: int, **kwargs: Any) -> None:
        _output[_index] = func(*args, **kwargs)

    return wrapped


def _applies_slice(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def wrapped(*args: Any, _indexer: Union[int, slice], **kwargs: Any) -> T:
        applier = partial(_maybe_slice, indexer=_indexer)
        return func(*CList(args).map(applier), **CDict(kwargs).map_values(applier))

    return wrapped


def _maybe_slice(x: Any, *, indexer: Union[int, slice]) -> Any:
    if isinstance(x, memmap):
        return x[indexer]
    else:
        return x


def _maybe_memmap(x: Any, path: Union[Path, str]) -> Any:
    if isinstance(x, ndarray):
        with atomic_write_path(path) as temp:
            joblib.dump(x, temp)
        return joblib.load(path, mmap_mode="r")
    else:
        return x


def _build_array_windower(
    func: Optional[Callable[..., Union[float, ndarray]]] = None,
    *,
    temp_dir: Union[Path, str] = TEMP_DIR,
) -> Callable[..., ndarray]:
    @wraps(func)
    def wrapped(
        *args: Any,
        window: int = 1,
        min_frac: Optional[float] = None,
        n_jobs: int = CPU_COUNT,
        **kwargs: Any,
    ) -> ndarray:
        if window <= 0:
            raise InvalidWindowError(f"Got window = {window}")

        applies_slice = _applies_slice(func)
        Path(temp_dir).mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(dir=temp_dir) as td:
            td = Path(td)

            # maybe memmap
            new_args: CList[Any] = (
                CList(args)
                .enumerate()
                .starmap(lambda i, v: _maybe_memmap(v, td.joinpath(f"arg_{i}")))
            )
            new_kwargs: CDict[str, Any] = CDict(kwargs).map_items(
                lambda k, v: (k, _maybe_memmap(v, td.joinpath(f"kwarg_{k}"))),
            )
            length = (
                new_args.chain(new_kwargs.values())
                .filter(lambda x: isinstance(x, memmap))
                .map(len)
                .set()
                .one()
            )
            if length == 0:
                raise ValueError("Expected non-zero length")

            # create indexers
            if window == 1:
                indexers: CList[int] = CList.range(length)
            else:
                indexers: CList[Optional[slice]] = CList.range(1, length + 1).map(
                    lambda x: slice(max(x - window, 0), x),
                )
                if min_frac is None:
                    indexers: CList[Optional[slice]] = indexers
                else:
                    min_length = min_frac * window
                    indexers = indexers.map(
                        lambda x: x if (x.stop - x.start) >= min_length else None,
                    )

            # apply last index
            *_, last_indexer = indexers
            if last_indexer is None:
                raise ValueError("Expected the last indexer to be a slice")
            last_result = applies_slice(*new_args, _indexer=last_indexer, **new_kwargs)
            last_array = array(last_result)

            # prepare output
            output = memmap(
                filename=str(td.joinpath("output")),
                dtype=last_array.dtype,
                mode="w+",
                shape=tuple(chain([length], last_array.shape)),
            )

            # apply all remaining slices
            Parallel(n_jobs=n_jobs)(
                delayed(_writes_output(applies_slice))(
                    *new_args, _indexer=indexer, _output=output, _index=index, **new_kwargs,
                )
                for index, indexer in enumerate(indexers)
                if indexer not in [None, last_indexer]
            )

        # NaN head and copy last result
        out_array = array(output)
        for i, _ in indexers.enumerate().filter(lambda x: x[1] is None):
            out_array[i] = nan
        out_array[-1] = last_result
        return out_array

    return wrapped


def ndarray_windower(
    func: Optional[Callable[..., Union[float, ndarray]]] = None,
    *,
    temp_dir: Union[Path, str] = TEMP_DIR,
) -> Callable[..., ndarray]:
    if func is None:
        return partial(ndarray_windower, temp_dir=temp_dir)
    else:
        return _build_array_windower(func, temp_dir=temp_dir)
