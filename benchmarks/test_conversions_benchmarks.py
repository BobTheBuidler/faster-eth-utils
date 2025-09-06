# mypy: disable-error-code=misc
# benchmarks/test_conversions_benchmarks.py
from typing import Any, Callable, List, Optional, Union, Tuple

import eth_utils
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils

def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)

to_hex_cases: List[Any] = [
    b"helloworld",  # bytes
    123456789,      # int
    True,           # bool
]
to_hex_ids = [
    "bytes",
    "int",
    "bool",
]

to_int_cases: List[Any] = [
    123456789,      # int
    True,           # bool
    b"\x07[\xcd\x15", # bytes (big-endian)
]
to_int_ids = [
    "int",
    "bool",
    "bytes",
]

to_bytes_cases: List[Any] = [
    123456789,      # int
    b"helloworld",  # bytes
    True,           # bool
]
to_bytes_ids = [
    "int",
    "bytes",
    "bool",
]

to_text_cases: List[Any] = [
    b"helloworld",  # bytes
    123456789,      # int
    "0x68656c6c6f", # str (should decode as hexstr)
]
to_text_ids = [
    "bytes",
    "int",
    "str-hex",
]

text_if_str_cases: List[Tuple[Any, ...]] = [
    ("helloworld",),  # str
    (b"helloworld",), # bytes
    (123456789,),     # int
]
text_if_str_ids = [
    "str",
    "bytes",
    "int",
]

hexstr_if_str_cases: List[Tuple[Any, ...]] = [
    ("0x68656c6c6f",),  # hexstr
    (b"helloworld",),   # bytes
    (123456789,),       # int
]
hexstr_if_str_ids = [
    "hexstr",
    "bytes",
    "int",
]

@pytest.mark.benchmark(group="to_hex")
@pytest.mark.parametrize("value", to_hex_cases, ids=to_hex_ids)
def test_to_hex(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, eth_utils.to_hex, value)

@pytest.mark.benchmark(group="to_hex")
@pytest.mark.parametrize("value", to_hex_cases, ids=to_hex_ids)
def test_faster_to_hex(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, faster_eth_utils.to_hex, value)

@pytest.mark.benchmark(group="to_int")
@pytest.mark.parametrize("value", to_int_cases, ids=to_int_ids)
def test_to_int(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, eth_utils.to_int, value)

@pytest.mark.benchmark(group="to_int")
@pytest.mark.parametrize("value", to_int_cases, ids=to_int_ids)
def test_faster_to_int(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, faster_eth_utils.to_int, value)

@pytest.mark.benchmark(group="to_bytes")
@pytest.mark.parametrize("value", to_bytes_cases, ids=to_bytes_ids)
def test_to_bytes(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, eth_utils.to_bytes, value)

@pytest.mark.benchmark(group="to_bytes")
@pytest.mark.parametrize("value", to_bytes_cases, ids=to_bytes_ids)
def test_faster_to_bytes(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, faster_eth_utils.to_bytes, value)

@pytest.mark.benchmark(group="to_text")
@pytest.mark.parametrize("value", to_text_cases, ids=to_text_ids)
def test_to_text(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, eth_utils.to_text, value)

@pytest.mark.benchmark(group="to_text")
@pytest.mark.parametrize("value", to_text_cases, ids=to_text_ids)
def test_faster_to_text(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, faster_eth_utils.to_text, value)

@pytest.mark.benchmark(group="text_if_str")
@pytest.mark.parametrize("args", text_if_str_cases, ids=text_if_str_ids)
def test_text_if_str(benchmark: BenchmarkFixture, args: Tuple[Any, ...]) -> None:
    benchmark(_batch, 10, eth_utils.text_if_str, eth_utils.to_text, *args)

@pytest.mark.benchmark(group="text_if_str")
@pytest.mark.parametrize("args", text_if_str_cases, ids=text_if_str_ids)
def test_faster_text_if_str(benchmark: BenchmarkFixture, args: Tuple[Any, ...]) -> None:
    benchmark(_batch, 10, faster_eth_utils.text_if_str, faster_eth_utils.to_text, *args)

@pytest.mark.benchmark(group="hexstr_if_str")
@pytest.mark.parametrize("args", hexstr_if_str_cases, ids=hexstr_if_str_ids)
def test_hexstr_if_str(benchmark: BenchmarkFixture, args: Tuple[Any, ...]) -> None:
    benchmark(_batch, 10, eth_utils.hexstr_if_str, eth_utils.to_hex, *args)

@pytest.mark.benchmark(group="hexstr_if_str")
@pytest.mark.parametrize("args", hexstr_if_str_cases, ids=hexstr_if_str_ids)
def test_faster_hexstr_if_str(benchmark: BenchmarkFixture, args: Tuple[Any, ...]) -> None:
    benchmark(_batch, 10, faster_eth_utils.hexstr_if_str, faster_eth_utils.to_hex, *args)
