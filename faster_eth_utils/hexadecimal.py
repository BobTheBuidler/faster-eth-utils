# String encodings and numeric representations

import binascii
import re
from typing import (
    Any,
    Final,
    TypeGuard,
)

from eth_typing import (
    HexStr,
)

_HEX_REGEXP_MATCH: Final = re.compile("(0[xX])?[0-9a-fA-F]*").fullmatch

_unhexlify: Final = binascii.unhexlify



def decode_hex(value: str) -> bytes:
    if not isinstance(value, str):
        raise TypeError("Value must be an instance of str")
    non_prefixed = remove_0x_prefix(HexStr(value))
    # unhexlify will only accept bytes type someday
    ascii_hex = non_prefixed.encode("ascii")
    return _unhexlify(ascii_hex)


def encode_hex(value: str | bytes | bytearray | memoryview) -> HexStr:
    if isinstance(value, str):
        encoded = value.encode("ascii").hex()
    elif isinstance(value, (bytes, bytearray, memoryview)):
        encoded = value.hex()
    else:
        raise TypeError("Value must be an instance of str or unicode")

    return add_0x_prefix(HexStr(encoded))


def is_0x_prefixed(value: str) -> bool:
    # this check is not needed in the compiled version
    # if not isinstance(value, str):
    #     raise TypeError(
    #         f"is_0x_prefixed requires text typed arguments. Got: {repr(value)}"
    #     )
    return value.startswith(("0x", "0X"))


def remove_0x_prefix(value: HexStr) -> HexStr:
    if is_0x_prefixed(value):
        return HexStr(value[2:])
    return value


def add_0x_prefix(value: HexStr) -> HexStr:
    if is_0x_prefixed(value):
        return value
    return HexStr("0x" + value)


def is_hexstr(value: Any) -> TypeGuard[HexStr]:
    if not isinstance(value, str) or not value:
        return False
    return _HEX_REGEXP_MATCH(value) is not None


def is_hex(value: Any) -> TypeGuard[HexStr]:
    if not isinstance(value, str):
        raise TypeError(f"is_hex requires text typed arguments. Got: {repr(value)}")
    if not value:
        return False
    return _HEX_REGEXP_MATCH(value) is not None
