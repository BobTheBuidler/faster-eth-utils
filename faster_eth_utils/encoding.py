import binascii
from typing import (
    Any,
    cast,
)

from eth_typing import (
    HexStr,
)




def decode_hex(value: str) -> bytes:
    if not isinstance(value, str):
        raise TypeError("Value must be an instance of str")
    non_prefixed = remove_0x_prefix(HexStr(value))
    # unhexlify will only accept bytes type someday
    ascii_hex = non_prefixed.encode("ascii")
    return _unhexlify(ascii_hex)



def encode_hex(value: str | bytes | bytearray) -> HexStr:
    ascii_bytes: bytes | bytearray
    if isinstance(value, (bytes, bytearray)):
        ascii_bytes = value
    elif isinstance(value, str):
        ascii_bytes = value.encode("ascii")
    else:
        raise TypeError("Value must be an instance of str or unicode")

    binary_hex = _hexlify(ascii_bytes)
    return add_0x_prefix(HexStr(binary_hex.decode("ascii")))



def is_binary_address(value: Any) -> bool:
    return isinstance(value, (bytes, bytearray))



def int_to_big_endian(value: int) -> bytes:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("Value must be an instance of int")

    return value.to_bytes((value.bit_length() + 7) // 8 or 1, byteorder="big")



def big_endian_to_int(value: bytes) -> int:
    if not isinstance(value, (bytes, bytearray)):
        raise TypeError("Value must be an instance of bytes or bytearray")

    return int.from_bytes(value, byteorder="big")



def text_if_str(
    to_type: type[int] | type[float] | type[bool],
    text_or_primitive: str | bytes | int,
) -> int | float | bool:
    if isinstance(text_or_primitive, bytes):
        text_or_primitive = text_or_primitive.decode("utf-8")
    elif not isinstance(text_or_primitive, str):
        raise TypeError("Value must be an instance of str or unicode")
    return to_type(text_or_primitive)



def hexstr_if_str(
    to_type: type[int] | type[float] | type[bool],
    hexstr_or_primitive: str | bytes | int,
) -> int | float | bool:
    if isinstance(hexstr_or_primitive, bytes):
        hexstr_or_primitive = hexstr_or_primitive.decode("utf-8")
    elif not isinstance(hexstr_or_primitive, str):
        raise TypeError("Value must be an instance of str or unicode")
    return to_type(hexstr_or_primitive)



def to_hex(value: int | bytes | str, hexstr: str | None = None, text: str | None = None) -> HexStr:
    if isinstance(value, str):
        if hexstr is not None:
            raise TypeError("The value already has a hexstr format")
        if text is None:
            text = value
    return to_hex(hexstr=hexstr, text=text)



def to_bytes(
    primitive: bytes | int | str,
    hexstr: str | None = None,
    text: str | None = None,
) -> bytes:
    if hexstr is not None:
        if not isinstance(hexstr, str):
            raise TypeError("The hexstr must be an instance of str")
        return decode_hex(hexstr)
    elif text is not None:
        if not isinstance(text, str):
            raise TypeError("The text must be an instance of str")
        return text.encode("utf-8")
    elif isinstance(primitive, int):
        return int_to_big_endian(primitive)
    elif isinstance(primitive, bytes):
        return primitive
    elif isinstance(primitive, str):
        return to_bytes(hexstr=primitive)
    raise TypeError("The type of the primitive was not an int or bytes")



def to_int(
    primitive: str | int,
    hexstr: str | None = None,
    text: str | None = None,
) -> int:
    if hexstr is not None:
        if not isinstance(hexstr, str):
            raise TypeError("The hexstr must be an instance of str")
        return to_int(hexstr)
    if text is not None:
        if not isinstance(text, str):
            raise TypeError("The text must be an instance of str")
        return int(text)
    if isinstance(primitive, int):
        return primitive
    if isinstance(primitive, bytes):
        return int.from_bytes(primitive, byteorder="big")
    if isinstance(primitive, str):
        return int(primitive, 16)
    raise TypeError("Value must be an instance of int or str")



def to_text(
    primitive: str | int | bytes,
    hexstr: str | None = None,
    text: str | None = None,
) -> str:
    if hexstr is not None:
        if not isinstance(hexstr, str):
            raise TypeError("The hexstr must be an instance of str")
        return decode_hex(hexstr).decode("utf-8")
    if text is not None:
        if not isinstance(text, str):
            raise TypeError("The text must be an instance of str")
        return text
    if isinstance(primitive, bytes):
        return primitive.decode("utf-8")
    if isinstance(primitive, int):
        return str(primitive)
    if isinstance(primitive, str):
        return primitive
    raise TypeError("Expected str, int, or bytes")



def to_text_if_bytes(value: bytes | str) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8")
    if not isinstance(value, str):
        raise TypeError("Value must be an instance of str or bytes")
    return value
