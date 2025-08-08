import collections
import functools
import itertools
from typing import (  # noqa: F401
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Set,
    Tuple,
    TypeVar,
    Union,
)

from typing_extensions import ParamSpec

from .toolz import (
    compose as _compose,
)

P = ParamSpec("P")
T = TypeVar("T")


def identity(value: T) -> T:
    return value


TGIn = TypeVar("TGIn")
TGOut = TypeVar("TGOut")
TFOut = TypeVar("TFOut")


def combine(
    f: Callable[[TGOut], TFOut], g: Callable[[TGIn], TGOut]
) -> Callable[[TGIn], TFOut]:
    def combined(x: TGIn) -> TFOut:
        return f(g(x))
    return combined


def apply_to_return_value(
    callback: Callable[P, T]
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def outer(fn: Callable[P, T]) -> Callable[P, T]:
        # We would need to type annotate *args and **kwargs but doing so segfaults
        # the PyPy builds. We ignore instead.
        @functools.wraps(fn)
        def inner(*args: P.args, **kwargs: P.kwargs) -> T:  # type: ignore
            return callback(fn(*args, **kwargs))

        return inner

    return outer


TVal = TypeVar("TVal")
TKey = TypeVar("TKey")

def to_tuple(fn: Callable[P, Iterable[TVal]]) -> Callable[P, Tuple[TVal, ...]]:
    def to_tuple_wrap(*args: P.args, **kwargs: P.kwargs) -> Tuple[TVal, ...]:
        return tuple(fn(*args, **kwargs))
    return to_tuple_wrap

def to_list(fn: Callable[P, Iterable[TVal]]) -> Callable[P, List[TVal]]:
    def to_list_wrap(*args: P.args, **kwargs: P.kwargs) -> T:
        return list(fn(*args, **kwargs))
    return to_list_wrap

def to_set(fn: Callable[P, Iterable[TVal]]) -> Callable[P, Set[TVal]]:
    def to_set_wrap(*args: P.args, **kwargs: P.kwargs) -> T:
        return set(fn(*args, **kwargs))
    return to_set_wrap

def to_dict(
    fn: Callable[P, Union[Mapping[TKey, TVal], Iterable[Tuple[TKey, TVal]]]]
) -> Callable[P, Dict[TKey, TVal]]:
    def to_dict_wrap(*args: P.args, **kwargs: P.kwargs) -> T:
        return dict(fn(*args, **kwargs))
    return to_dict_wrap

to_ordered_dict = apply_to_return_value(
    collections.OrderedDict
)  # type: Callable[[Callable[..., Iterable[Union[Mapping[TKey, TVal], Tuple[TKey, TVal]]]]], Callable[..., collections.OrderedDict[TKey, TVal]]]  # noqa: E501
sort_return = _compose(to_tuple, apply_to_return_value(sorted))
flatten_return = _compose(
    to_tuple, apply_to_return_value(itertools.chain.from_iterable)
)
reversed_return = _compose(to_tuple, apply_to_return_value(reversed), to_tuple)
