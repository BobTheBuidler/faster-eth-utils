# mypy: disable-error-code=misc
from typing import Any, Callable, Dict, List, Tuple

import eth_utils
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils

def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)


# apply_formatter_at_index: valid and out-of-bounds
afi_cases = [
    (lambda x: x + 1, 0, [1, 2, 3]),  # valid
    (lambda x: x + 1, 2, [1, 2, 3]),  # valid
    (lambda x: x + 1, 3, [1, 2, 3]),  # out-of-bounds (should raise)
]

# combine_argument_formatters: 1 and 2 formatters
caf_cases = [
    (lambda x: x + 1,),
    (lambda x: x + 1, lambda x: x * 2),
]

# apply_formatters_to_sequence: equal, too many, too few formatters
afts_cases = [
    ([lambda x: x + 1, lambda x: x * 2], [1, 2]),  # equal
    ([lambda x: x + 1, lambda x: x * 2, lambda x: x - 1], [1, 2]),  # too many
    ([lambda x: x + 1], [1, 2]),  # too few
]

# apply_formatter_if: condition true and false
afi_if_cases = [
    (lambda x: x > 0, lambda x: x * 2, 2),  # true
    (lambda x: x > 0, lambda x: x * 2, -1),  # false
]

# apply_formatters_to_dict: key present, key not present, formatter raises error
af2d_cases = [
    ({"a": lambda x: x + 1, "b": lambda x: x * 2}, {"a": 1, "b": 2}),  # all keys present
    ({"a": lambda x: x + 1}, {"a": 1, "b": 2}),  # key not present in formatters
    ({"a": lambda x: int("notanint")}, {"a": 1}),  # formatter raises error
]

# apply_formatter_to_array: just typical
afta_cases = [
    (lambda x: x + 1, [1, 2, 3]),
]

# apply_one_of_formatters: first matches, second matches, none match
aoof_cases = [
    (((lambda x: x > 0, lambda x: x * 2), (lambda x: x < 0, lambda x: x - 2)), 2),  # first matches
    (((lambda x: x < 0, lambda x: x - 2), (lambda x: x > 0, lambda x: x * 2)), 2),  # second matches
    (((lambda x: x < 0, lambda x: x - 2), (lambda x: x > 10, lambda x: x * 2)), 2),  # none match (should raise)
]

# apply_key_map: no conflict, conflict (should raise)
akm_cases = [
    ({"a": "b"}, {"a": 1}),  # no conflict
    ({"a": "b"}, {"a": 1, "b": 2}),  # conflict (should raise)
]

@pytest.mark.benchmark(group="apply_formatter_at_index")
@pytest.mark.parametrize("formatter,at_index,value", afi_cases)
def test_apply_formatter_at_index(
    benchmark: BenchmarkFixture,
    formatter: Callable[[int], int],
    at_index: int,
    value: List[int]
) -> None:
    benchmark(_batch, 10, eth_utils.apply_formatter_at_index, formatter, at_index, value)

@pytest.mark.benchmark(group="apply_formatter_at_index")
@pytest.mark.parametrize("formatter,at_index,value", afi_cases)
def test_faster_apply_formatter_at_index(
    benchmark: BenchmarkFixture,
    formatter: Callable[[int], int],
    at_index: int,
    value: List[int]
) -> None:
    benchmark(_batch, 10, faster_eth_utils.apply_formatter_at_index, formatter, at_index, value)

@pytest.mark.benchmark(group="combine_argument_formatters")
@pytest.mark.parametrize("formatters", caf_cases)
def test_combine_argument_formatters(
    benchmark: BenchmarkFixture,
    formatters: Tuple[Callable[[int], int], ...]
) -> None:
    benchmark(_batch, 10, eth_utils.combine_argument_formatters, *formatters)

@pytest.mark.benchmark(group="combine_argument_formatters")
@pytest.mark.parametrize("formatters", caf_cases)
def test_faster_combine_argument_formatters(
    benchmark: BenchmarkFixture,
    formatters: Tuple[Callable[[int], int], ...]
) -> None:
    benchmark(_batch, 10, faster_eth_utils.combine_argument_formatters, *formatters)

@pytest.mark.benchmark(group="apply_formatters_to_sequence")
@pytest.mark.parametrize("formatters,sequence", afts_cases)
def test_apply_formatters_to_sequence(
    benchmark: BenchmarkFixture,
    formatters: List[Callable[[int], int]],
    sequence: List[int]
) -> None:
    benchmark(_batch, 10, eth_utils.apply_formatters_to_sequence, formatters, sequence)

@pytest.mark.benchmark(group="apply_formatters_to_sequence")
@pytest.mark.parametrize("formatters,sequence", afts_cases)
def test_faster_apply_formatters_to_sequence(
    benchmark: BenchmarkFixture,
    formatters: List[Callable[[int], int]],
    sequence: List[int]
) -> None:
    benchmark(_batch, 10, faster_eth_utils.apply_formatters_to_sequence, formatters, sequence)

@pytest.mark.benchmark(group="apply_formatter_if")
@pytest.mark.parametrize("pred,formatter,value", afi_if_cases)
def test_apply_formatter_if(
    benchmark: BenchmarkFixture,
    pred: Callable[[int], bool],
    formatter: Callable[[int], int],
    value: int
) -> None:
    benchmark(_batch, 10, eth_utils.apply_formatter_if, pred, formatter, value)

@pytest.mark.benchmark(group="apply_formatter_if")
@pytest.mark.parametrize("pred,formatter,value", afi_if_cases)
def test_faster_apply_formatter_if(
    benchmark: BenchmarkFixture,
    pred: Callable[[int], bool],
    formatter: Callable[[int], int],
    value: int
) -> None:
    benchmark(_batch, 10, faster_eth_utils.apply_formatter_if, pred, formatter, value)

@pytest.mark.benchmark(group="apply_formatters_to_dict")
@pytest.mark.parametrize("formatters,value", af2d_cases)
def test_apply_formatters_to_dict(
    benchmark: BenchmarkFixture,
    formatters: Dict[str, Callable[[int], int]],
    value: Dict[str, int]
) -> None:
    benchmark(_batch, 10, eth_utils.apply_formatters_to_dict, formatters, value)

@pytest.mark.benchmark(group="apply_formatters_to_dict")
@pytest.mark.parametrize("formatters,value", af2d_cases)
def test_faster_apply_formatters_to_dict(
    benchmark: BenchmarkFixture,
    formatters: Dict[str, Callable[[int], int]],
    value: Dict[str, int]
) -> None:
    benchmark(_batch, 10, faster_eth_utils.apply_formatters_to_dict, formatters, value)

@pytest.mark.benchmark(group="apply_formatter_to_array")
@pytest.mark.parametrize("formatter,value", afta_cases)
def test_apply_formatter_to_array(
    benchmark: BenchmarkFixture,
    formatter: Callable[[int], int],
    value: List[int]
) -> None:
    benchmark(_batch, 10, eth_utils.apply_formatter_to_array, formatter, value)

@pytest.mark.benchmark(group="apply_formatter_to_array")
@pytest.mark.parametrize("formatter,value", afta_cases)
def test_faster_apply_formatter_to_array(
    benchmark: BenchmarkFixture,
    formatter: Callable[[int], int],
    value: List[int]
) -> None:
    benchmark(_batch, 10, faster_eth_utils.apply_formatter_to_array, formatter, value)

@pytest.mark.benchmark(group="apply_one_of_formatters")
@pytest.mark.parametrize("formatter_condition_pairs,value", aoof_cases)
def test_apply_one_of_formatters(
    benchmark: BenchmarkFixture,
    formatter_condition_pairs: Tuple[Tuple[Callable[[int], bool], Callable[[int], int]], ...],
    value: int
) -> None:
    benchmark(_batch, 10, eth_utils.apply_one_of_formatters, formatter_condition_pairs, value)

@pytest.mark.benchmark(group="apply_one_of_formatters")
@pytest.mark.parametrize("formatter_condition_pairs,value", aoof_cases)
def test_faster_apply_one_of_formatters(
    benchmark: BenchmarkFixture,
    formatter_condition_pairs: Tuple[Tuple[Callable[[int], bool], Callable[[int], int]], ...],
    value: int
) -> None:
    benchmark(_batch, 10, faster_eth_utils.apply_one_of_formatters, formatter_condition_pairs, value)

@pytest.mark.benchmark(group="apply_key_map")
@pytest.mark.parametrize("key_map,value", akm_cases)
def test_apply_key_map(
    benchmark: BenchmarkFixture,
    key_map: Dict[str, str],
    value: Dict[str, int]
) -> None:
    benchmark(_batch, 10, eth_utils.apply_key_map, key_map, value)

@pytest.mark.benchmark(group="apply_key_map")
@pytest.mark.parametrize("key_map,value", akm_cases)
def test_faster_apply_key_map(
    benchmark: BenchmarkFixture,
    key_map: Dict[str, str],
    value: Dict[str, int]
) -> None:
    benchmark(_batch, 10, faster_eth_utils.apply_key_map, key_map, value)
