import collections.abc
import numbers
from typing import (
    Any,
    Literal,
    TypeGuard,
    Union,
)

bytes_types = (bytes, bytearray)
integer_types = (int,)
text_types = (str,)
string_types = (bytes, str, bytearray)


def is_integer(value: Any) -> TypeGuard[int]:
    return isinstance(value, integer_types) and not isinstance(value, bool)


def is_bytes(value: Any) -> TypeGuard[Union[bytes, bytearray]]:
    return isinstance(value, bytes_types)


def is_text(value: Any) -> TypeGuard[str]:
    return isinstance(value, text_types)


def is_string(value: Any) -> TypeGuard[Union[bytes, str, bytearray]]:
    return isinstance(value, string_types)


def is_boolean(value: Any) -> TypeGuard[bool]:
    return isinstance(value, bool)


def is_dict(obj: Any) -> TypeGuard[collections.abc.Mapping]:
    return isinstance(obj, collections.abc.Mapping)


def is_list_like(obj: Any) -> TypeGuard[collections.abc.Sequence]:
    return not is_string(obj) and isinstance(obj, collections.abc.Sequence)


def is_list(obj: Any) -> TypeGuard[list]:
    return isinstance(obj, list)


def is_tuple(obj: Any) -> TypeGuard[tuple]:
    return isinstance(obj, tuple)


def is_null(obj: Any) -> TypeGuard[Literal[None]]:
    return obj is None


def is_number(obj: Any) -> TypeGuard[numbers.Number]:
    return isinstance(obj, numbers.Number)
