import collections
import itertools
from collections.abc import Callable, Iterable, Mapping
from functools import wraps
from typing import (  # noqa: F401
    Dict,
    Final,
    List,
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

_OrderedDict: Final = collections.OrderedDict

_chain_from_iterable: Final = itertools.chain.from_iterable


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


TCb = TypeVar("TCb")


def apply_to_return_value(
    callback: Callable[[T], TCb]
) -> Callable[[Callable[P, T]], Callable[P, TCb]]:
    def outer(fn: Callable[P, T]) -> Callable[P, TCb]:
        @wraps(fn)
        def inner(*args: P.args, **kwargs: P.kwargs) -> TCb:
            return callback(fn(*args, **kwargs))
        return inner
    return outer


TVal = TypeVar("TVal")
TKey = TypeVar("TKey")

def to_tuple(fn: Callable[P, Iterable[TVal]]) -> Callable[P, tuple[TVal, ...]]:
    def to_tuple_wrap(*args: P.args, **kwargs: P.kwargs) -> tuple[TVal, ...]:
        return tuple(fn(*args, **kwargs))
    return to_tuple_wrap

def to_list(fn: Callable[P, Iterable[TVal]]) -> Callable[P, list[TVal]]:
    def to_list_wrap(*args: P.args, **kwargs: P.kwargs) -> list[TVal]:
        return list(fn(*args, **kwargs))
    return to_list_wrap

def to_set(fn: Callable[P, Iterable[TVal]]) -> Callable[P, set[TVal]]:
    def to_set_wrap(*args: P.args, **kwargs: P.kwargs) -> set[TVal]:
        return set(fn(*args, **kwargs))
    return to_set_wrap

def to_dict(
    fn: Callable[P, Mapping[TKey, TVal] | Iterable[tuple[TKey, TVal]]]
) -> Callable[P, dict[TKey, TVal]]:
    def to_dict_wrap(*args: P.args, **kwargs: P.kwargs) -> dict[TKey, TVal]:
        return dict(fn(*args, **kwargs))
    return to_dict_wrap

to_ordered_dict = apply_to_return_value(  # type: ignore [assignment]
    _OrderedDict
)  # type: Callable[[Callable[P, Union[Mapping[TKey, TVal], Iterable[Tuple[TKey, TVal]]]]], Callable[P, collections.OrderedDict[TKey, TVal]]]  # noqa: E501
sort_return = _compose(to_tuple, apply_to_return_value(sorted))
flatten_return = _compose(
    to_tuple, apply_to_return_value(_chain_from_iterable)
)
reversed_return = _compose(to_tuple, apply_to_return_value(reversed), to_tuple)
