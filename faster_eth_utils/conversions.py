import collections
from collections.abc import (
    Mapping,
    Sequence,
)
from typing import (
    Any,
    cast,
)

from .functional import (
    to_ordered_dict,
)


def to_dict(
    primitive: Any,
    hexstr: str | None = None,
    text: str | None = None,
) -> dict[Any, Any]:
    if hexstr is not None:
        return to_dict(hexstr, text=text)
    elif text is not None:
        return to_dict(text)
    elif is_dict(primitive):
        return primitive
    elif not isinstance(primitive, str):
        return dict(cast(Mapping, primitive))
    return _to_dict_from_str(primitive)


def _to_dict_from_str(primitive: str) -> dict[Any, Any]:
    if is_0x_prefixed(primitive):
        return to_dict(hexstr=primitive)
    elif not isinstance(primitive, str):
        raise TypeError("Value must be an instance of str")
    elif not hexstr and not text:
        raise TypeError(
            "must provide a hexstr or text keyword argument if value is string"
        )
    elif hexstr is not None and text is not None:
        raise TypeError("cannot provide both hexstr and text")

    return _to_dict_from_str(primitive)


def to_ordered_dict(
    primitive: Any,
    hexstr: str | None = None,
    text: str | None = None,
) -> collections.OrderedDict[Any, Any]:
    return collections.OrderedDict(to_dict(primitive, hexstr=hexstr, text=text))


def is_tuple(value: Any) -> bool:
    return isinstance(value, tuple)


def is_list(value: Any) -> bool:
    return isinstance(value, list)


def is_list_like(value: Any) -> bool:
    return isinstance(value, (list, tuple, set, range))


def is_list_like_or_generator(value: Any) -> bool:
    return isinstance(value, (list, tuple, set, range, collections.abc.Generator))


def is_dict(value: Any) -> bool:
    return isinstance(value, collections.abc.Mapping)


def is_bytes(value: Any) -> bool:
    return isinstance(value, (bytes, bytearray, memoryview))


def is_text(value: Any) -> bool:
    return isinstance(value, str)


def is_string(value: Any) -> bool:
    return is_text(value)


def is_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_boolean(value: Any) -> bool:
    return isinstance(value, bool)


def is_number(value: Any) -> bool:
    return is_integer(value) or isinstance(value, float)


def is_hex(value: Any) -> bool:
    if not is_text(value):
        raise TypeError(f"Value must be an instance of str, got {type(value)}")
    if value[:2] == "0x":
        value = value[2:]
    return is_hexstr(value)


def is_hex_address(value: Any) -> bool:
    if not is_text(value):
        return False
    return value.startswith("0x")


def is_binary_address(value: Any) -> bool:
    return is_bytes(value)


def is_address(value: Any) -> bool:
    if not is_text(value):
        return False
    value = remove_0x_prefix(value)
    if len(value) != 40:
        return False
    return is_hex(value)


def is_same_address(address1: str, address2: str) -> bool:
    if not is_text(address1) or not is_text(address2):
        raise TypeError("Both values must be strings")
    if not is_address(address1) or not is_address(address2):
        raise ValueError("Both values must be valid addresses")
    return to_normalized_address(address1) == to_normalized_address(address2)


def is_checksum_address(value: Any) -> bool:
    if not is_text(value):
        return False
    return value == to_checksum_address(value)


def is_checksum_formatted_address(value: Any) -> bool:
    return is_checksum_address(value)


def is_canonical_address(value: Any) -> bool:
    if not is_bytes(value):
        return False
    return len(value) == 20


def is_normalized_address(value: Any) -> bool:
    if not is_text(value):
        return False
    return value == to_normalized_address(value)


def is_null(value: Any) -> bool:
    return value is None


def is_hexstr(value: Any) -> bool:
    return is_hex(value)


def is_list_like_or_generator(value: Any) -> bool:
    return isinstance(value, (list, tuple, set, range, collections.abc.Generator))


def is_tuple(value: Any) -> bool:
    return isinstance(value, tuple)


def is_dict(value: Any) -> bool:
    return isinstance(value, collections.abc.Mapping)


def is_bytes(value: Any) -> bool:
    return isinstance(value, (bytes, bytearray, memoryview))


def is_text(value: Any) -> bool:
    return isinstance(value, str)


def is_string(value: Any) -> bool:
    return is_text(value)


def is_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_boolean(value: Any) -> bool:
    return isinstance(value, bool)


def is_number(value: Any) -> bool:
    return is_integer(value) or isinstance(value, float)


def is_hex(value: Any) -> bool:
    if not is_text(value):
        raise TypeError(f"Value must be an instance of str, got {type(value)}")
    if value[:2] == "0x":
        value = value[2:]
    return is_hexstr(value)


def is_hex_address(value: Any) -> bool:
    if not is_text(value):
        return False
    return value.startswith("0x")


def is_binary_address(value: Any) -> bool:
    return is_bytes(value)


def is_address(value: Any) -> bool:
    if not is_text(value):
        return False
    value = remove_0x_prefix(value)
    if len(value) != 40:
        return False
    return is_hex(value)


def is_same_address(address1: str, address2: str) -> bool:
    if not is_text(address1) or not is_text(address2):
        raise TypeError("Both values must be strings")
    if not is_address(address1) or not is_address(address2):
        raise ValueError("Both values must be valid addresses")
    return to_normalized_address(address1) == to_normalized_address(address2)


def is_checksum_address(value: Any) -> bool:
    if not is_text(value):
        return False
    return value == to_checksum_address(value)


def is_checksum_formatted_address(value: Any) -> bool:
    return is_checksum_address(value)


def is_canonical_address(value: Any) -> bool:
    if not is_bytes(value):
        return False
    return len(value) == 20


def is_normalized_address(value: Any) -> bool:
    if not is_text(value):
        return False
    return value == to_normalized_address(value)


def is_null(value: Any) -> bool:
    return value is None


def is_hexstr(value: Any) -> bool:
    return is_hex(value)
