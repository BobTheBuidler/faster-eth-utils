# mypy: disable-error-code=misc
from typing import Any, Callable

import eth_utils
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils

def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)

is_integer_cases = [
    123,        # True
    True,       # False (bool is not int)
    1.5,        # False
    "abc",      # False
]

is_bytes_cases = [
    b"abc",     # True
    bytearray(b"abc"),  # True
    "abc",      # False
    123,        # False
]

is_text_cases = [
    "abc",      # True
    b"abc",     # False
    123,        # False
]

is_string_cases = [
    "abc",      # True
    b"abc",     # True
    bytearray(b"abc"),  # True
    123,        # False
]

is_boolean_cases = [
    True,       # True
    False,      # True
    1,          # False
    "abc",      # False
]

is_dict_cases = [
    {"a": 1},   # True
    [("a", 1)], # False
    123,        # False
]

is_list_like_cases = [
    [1, 2, 3],  # True
    (1, 2, 3),  # True
    "abc",      # False
    123,        # False
]

is_list_cases = [
    [1, 2, 3],  # True
    (1, 2, 3),  # False
    "abc",      # False
]

is_tuple_cases = [
    (1, 2, 3),  # True
    [1, 2, 3],  # False
    "abc",      # False
]

is_null_cases = [
    None,       # True
    0,          # False
    "",         # False
]

is_number_cases = [
    123,        # True
    1.5,        # True
    "abc",      # False
    [1, 2, 3],  # False
]

@pytest.mark.benchmark(group="is_integer")
@pytest.mark.parametrize("value", is_integer_cases)
def test_is_integer(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_integer, value)

@pytest.mark.benchmark(group="is_integer")
@pytest.mark.parametrize("value", is_integer_cases)
def test_faster_is_integer(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_integer, value)

@pytest.mark.benchmark(group="is_bytes")
@pytest.mark.parametrize("value", is_bytes_cases)
def test_is_bytes(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_bytes, value)

@pytest.mark.benchmark(group="is_bytes")
@pytest.mark.parametrize("value", is_bytes_cases)
def test_faster_is_bytes(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_bytes, value)

@pytest.mark.benchmark(group="is_text")
@pytest.mark.parametrize("value", is_text_cases)
def test_is_text(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_text, value)

@pytest.mark.benchmark(group="is_text")
@pytest.mark.parametrize("value", is_text_cases)
def test_faster_is_text(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_text, value)

@pytest.mark.benchmark(group="is_string")
@pytest.mark.parametrize("value", is_string_cases)
def test_is_string(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_string, value)

@pytest.mark.benchmark(group="is_string")
@pytest.mark.parametrize("value", is_string_cases)
def test_faster_is_string(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_string, value)

@pytest.mark.benchmark(group="is_boolean")
@pytest.mark.parametrize("value", is_boolean_cases)
def test_is_boolean(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_boolean, value)

@pytest.mark.benchmark(group="is_boolean")
@pytest.mark.parametrize("value", is_boolean_cases)
def test_faster_is_boolean(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_boolean, value)

@pytest.mark.benchmark(group="is_dict")
@pytest.mark.parametrize("value", is_dict_cases)
def test_is_dict(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_dict, value)

@pytest.mark.benchmark(group="is_dict")
@pytest.mark.parametrize("value", is_dict_cases)
def test_faster_is_dict(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_dict, value)

@pytest.mark.benchmark(group="is_list_like")
@pytest.mark.parametrize("value", is_list_like_cases)
def test_is_list_like(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_list_like, value)

@pytest.mark.benchmark(group="is_list_like")
@pytest.mark.parametrize("value", is_list_like_cases)
def test_faster_is_list_like(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_list_like, value)

@pytest.mark.benchmark(group="is_list")
@pytest.mark.parametrize("value", is_list_cases)
def test_is_list(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_list, value)

@pytest.mark.benchmark(group="is_list")
@pytest.mark.parametrize("value", is_list_cases)
def test_faster_is_list(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_list, value)

@pytest.mark.benchmark(group="is_tuple")
@pytest.mark.parametrize("value", is_tuple_cases)
def test_is_tuple(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_tuple, value)

@pytest.mark.benchmark(group="is_tuple")
@pytest.mark.parametrize("value", is_tuple_cases)
def test_faster_is_tuple(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_tuple, value)

@pytest.mark.benchmark(group="is_null")
@pytest.mark.parametrize("value", is_null_cases)
def test_is_null(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_null, value)

@pytest.mark.benchmark(group="is_null")
@pytest.mark.parametrize("value", is_null_cases)
def test_faster_is_null(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_null, value)

@pytest.mark.benchmark(group="is_number")
@pytest.mark.parametrize("value", is_number_cases)
def test_is_number(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, eth_utils.is_number, value)

@pytest.mark.benchmark(group="is_number")
@pytest.mark.parametrize("value", is_number_cases)
def test_faster_is_number(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 100, faster_eth_utils.is_number, value)
