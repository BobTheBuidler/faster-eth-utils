# String encodings and numeric representations

import binascii
import re
from typing import (
    Any,
    AnyStr,
    Final,
    TypeGuard,
)

from eth_typing import (
    HexStr,
)


hexlify: Final = binascii.hexlify
unhexlify: Final = binascii.unhexlify


# Precomputed table for ASCII hex digit lookup (0-9, a-f, A-F)
__TABLE = bytearray(128)
for _val in range(ord("0"), ord("9") + 1):
    __TABLE[_val] = 1
for _val in range(ord("a"), ord("f") + 1):
    __TABLE[_val] = 1
for _val in range(ord("A"), ord("F") + 1):
    __TABLE[_val] = 1
_HEX_DIGIT_TABLE = bytes(__TABLE)
del __TABLE


def decode_hex(value: str) -> bytes:
    if not isinstance(value, str):
        raise TypeError("Value must be an instance of str")
    non_prefixed = remove_0x_prefix(HexStr(value))
    # unhexlify will only accept bytes type someday
    ascii_hex = non_prefixed.encode("ascii")
    return unhexlify(ascii_hex)


def encode_hex(value: AnyStr) -> HexStr:
    ascii_bytes: bytes | bytearray
    if isinstance(value, (bytes, bytearray)):
        ascii_bytes = value
    elif isinstance(value, str):
        ascii_bytes = value.encode("ascii")
    else:
        raise TypeError("Value must be an instance of str or unicode")

    binary_hex = hexlify(ascii_bytes)
    return add_0x_prefix(HexStr(binary_hex.decode("ascii")))


def is_0x_prefixed(value: str) -> bool:
    # this check is not needed in the compiled version
    # if not isinstance(value, str):
    #     raise TypeError(
    #         f"is_0x_prefixed requires text typed arguments. Got: {repr(value)}"
    #     )
    return value.startswith(("0x", "0X"))


def remove_0x_prefix(value: HexStr) -> HexStr:
    return HexStr(value[2:]) if is_0x_prefixed(value) else value


def add_0x_prefix(value: HexStr) -> HexStr:
    return value if is_0x_prefixed(value) else HexStr(f"0x{value}")


def is_ascii(string: str) -> bool:
    for char in string:
        code = ord(char)
        if code >= 128 or _HEX_DIGIT_TABLE[code] == 0:
            return False
    return True


def is_hexstr(value: Any) -> TypeGuard[HexStr]:
    if not isinstance(value, str) or not value:
        return False
    return is_ascii(value[2:] if is_0x_prefixed(value) else value)


def is_hex(value: Any) -> TypeGuard[HexStr]:
    if not isinstance(value, str):
        raise TypeError(f"is_hex requires text typed arguments. Got: {repr(value)}")
    if not value:
        return False
    return is_ascii(value[2:] if is_0x_prefixed(value) else value)
