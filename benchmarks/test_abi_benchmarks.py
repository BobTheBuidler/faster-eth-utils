# mypy: disable-error-code=misc
from typing import Any, Callable, List, Dict

import eth_utils
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils


def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)

# Parameter lists for typical-case coverage

abi_elements: List[Dict[str, Any]] = [
    # Function ABI
    {
        "type": "function",
        "name": "transfer",
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"},
        ],
        "outputs": [{"name": "success", "type": "bool"}],
    },
    # Event ABI
    {
        "type": "event",
        "name": "Approval",
        "inputs": [
            {"name": "owner", "type": "address"},
            {"name": "spender", "type": "address"},
            {"name": "value", "type": "uint256"},
        ],
    },
    # Constructor ABI
    {
        "type": "constructor",
        "inputs": [{"name": "param", "type": "uint256"}],
    },
    # Fallback ABI
    {
        "type": "fallback",
    },
    # Receive ABI
    {
        "type": "receive",
    },
]

# For filter_abi_by_name: one that matches, one that doesn't
abi_names: List[str] = ["transfer", "nonexistent"]

# For filter_abi_by_type: function, event, and a type not present
abi_types: List[str] = ["function", "event", "error"]

# For get_all_function_abis and get_all_event_abis: normal and empty ABI lists
abi_lists: List[List[Dict[str, Any]]] = [
    [abi_elements[0], abi_elements[1]],  # function and event
    [],  # empty ABI
]

function_signatures: List[str] = [
    "transfer(address,uint256)",
    "approve(address,uint256)",
    "mint(address,uint256)",
]

event_signatures: List[str] = [
    "Approval(address,address,uint256)",
    "Transfer(address,address,uint256)",
]

@pytest.mark.benchmark(group="abi_to_signature")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_abi_to_signature(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.abi_to_signature, abi_element)

@pytest.mark.benchmark(group="abi_to_signature")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_abi_to_signature(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.abi_to_signature, abi_element)

@pytest.mark.benchmark(group="collapse_if_tuple")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_collapse_if_tuple(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.collapse_if_tuple, abi_element)

@pytest.mark.benchmark(group="collapse_if_tuple")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_collapse_if_tuple(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.collapse_if_tuple, abi_element)

@pytest.mark.benchmark(group="filter_abi_by_name")
@pytest.mark.parametrize("name,abi", [
    ("transfer", [abi_elements[0], abi_elements[1]]),  # should match
    ("nonexistent", [abi_elements[0], abi_elements[1]]),  # should not match
])
def test_filter_abi_by_name(benchmark: BenchmarkFixture, name: str, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, eth_utils.filter_abi_by_name, name, abi)

@pytest.mark.benchmark(group="filter_abi_by_name")
@pytest.mark.parametrize("name,abi", [
    ("transfer", [abi_elements[0], abi_elements[1]]),
    ("nonexistent", [abi_elements[0], abi_elements[1]]),
])
def test_faster_filter_abi_by_name(benchmark: BenchmarkFixture, name: str, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, faster_eth_utils.filter_abi_by_name, name, abi)

@pytest.mark.benchmark(group="filter_abi_by_type")
@pytest.mark.parametrize("type_,abi", [
    ("function", [abi_elements[0], abi_elements[1]]),  # present
    ("event", [abi_elements[0], abi_elements[1]]),     # present
    ("error", [abi_elements[0], abi_elements[1]]),     # not present
])
def test_filter_abi_by_type(benchmark: BenchmarkFixture, type_: str, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, eth_utils.filter_abi_by_type, type_, abi)

@pytest.mark.benchmark(group="filter_abi_by_type")
@pytest.mark.parametrize("type_,abi", [
    ("function", [abi_elements[0], abi_elements[1]]),
    ("event", [abi_elements[0], abi_elements[1]]),
    ("error", [abi_elements[0], abi_elements[1]]),
])
def test_faster_filter_abi_by_type(benchmark: BenchmarkFixture, type_: str, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, faster_eth_utils.filter_abi_by_type, type_, abi)

@pytest.mark.benchmark(group="get_all_function_abis")
@pytest.mark.parametrize("abi", abi_lists)
def test_get_all_function_abis(benchmark: BenchmarkFixture, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, eth_utils.get_all_function_abis, abi)

@pytest.mark.benchmark(group="get_all_function_abis")
@pytest.mark.parametrize("abi", abi_lists)
def test_faster_get_all_function_abis(benchmark: BenchmarkFixture, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, faster_eth_utils.get_all_function_abis, abi)

@pytest.mark.benchmark(group="get_all_event_abis")
@pytest.mark.parametrize("abi", abi_lists)
def test_get_all_event_abis(benchmark: BenchmarkFixture, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, eth_utils.get_all_event_abis, abi)

@pytest.mark.benchmark(group="get_all_event_abis")
@pytest.mark.parametrize("abi", abi_lists)
def test_faster_get_all_event_abis(benchmark: BenchmarkFixture, abi: List[Dict[str, Any]]) -> None:
    benchmark(_batch, 100, faster_eth_utils.get_all_event_abis, abi)

@pytest.mark.benchmark(group="get_normalized_abi_inputs")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_get_normalized_abi_inputs(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.get_normalized_abi_inputs, abi_element, 10, 10)

@pytest.mark.benchmark(group="get_normalized_abi_inputs")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_get_normalized_abi_inputs(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.get_normalized_abi_inputs, abi_element, 10, 10)

@pytest.mark.benchmark(group="get_aligned_abi_inputs")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_get_aligned_abi_inputs(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    normalized_inputs = faster_eth_utils.get_normalized_abi_inputs(abi_element, 10, 10)
    benchmark(_batch, 100, eth_utils.get_aligned_abi_inputs, abi_element, normalized_inputs)

@pytest.mark.benchmark(group="get_aligned_abi_inputs")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_get_aligned_abi_inputs(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    normalized_inputs = faster_eth_utils.get_normalized_abi_inputs(abi_element, 10, 10)
    benchmark(_batch, 100, faster_eth_utils.get_aligned_abi_inputs, abi_element, normalized_inputs)

@pytest.mark.benchmark(group="get_abi_input_names")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_get_abi_input_names(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.get_abi_input_names, abi_element)

@pytest.mark.benchmark(group="get_abi_input_names")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_get_abi_input_names(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.get_abi_input_names, abi_element)

@pytest.mark.benchmark(group="get_abi_input_types")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_get_abi_input_types(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.get_abi_input_types, abi_element)

@pytest.mark.benchmark(group="get_abi_input_types")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_get_abi_input_types(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.get_abi_input_types, abi_element)

@pytest.mark.benchmark(group="get_abi_output_names")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_get_abi_output_names(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.get_abi_output_names, abi_element)

@pytest.mark.benchmark(group="get_abi_output_names")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_get_abi_output_names(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.get_abi_output_names, abi_element)

@pytest.mark.benchmark(group="get_abi_output_types")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_get_abi_output_types(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.get_abi_output_types, abi_element)

@pytest.mark.benchmark(group="get_abi_output_types")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_get_abi_output_types(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.get_abi_output_types, abi_element)

@pytest.mark.benchmark(group="function_signature_to_4byte_selector")
@pytest.mark.parametrize("signature", function_signatures)
def test_function_signature_to_4byte_selector(benchmark: BenchmarkFixture, signature: str) -> None:
    benchmark(_batch, 100, eth_utils.function_signature_to_4byte_selector, signature)

@pytest.mark.benchmark(group="function_signature_to_4byte_selector")
@pytest.mark.parametrize("signature", function_signatures)
def test_faster_function_signature_to_4byte_selector(benchmark: BenchmarkFixture, signature: str) -> None:
    benchmark(_batch, 100, faster_eth_utils.function_signature_to_4byte_selector, signature)

@pytest.mark.benchmark(group="function_abi_to_4byte_selector")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_function_abi_to_4byte_selector(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.function_abi_to_4byte_selector, abi_element)

@pytest.mark.benchmark(group="function_abi_to_4byte_selector")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_function_abi_to_4byte_selector(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.function_abi_to_4byte_selector, abi_element)

@pytest.mark.benchmark(group="event_signature_to_log_topic")
@pytest.mark.parametrize("signature", event_signatures)
def test_event_signature_to_log_topic(benchmark: BenchmarkFixture, signature: str) -> None:
    benchmark(_batch, 100, eth_utils.event_signature_to_log_topic, signature)

@pytest.mark.benchmark(group="event_signature_to_log_topic")
@pytest.mark.parametrize("signature", event_signatures)
def test_faster_event_signature_to_log_topic(benchmark: BenchmarkFixture, signature: str) -> None:
    benchmark(_batch, 100, faster_eth_utils.event_signature_to_log_topic, signature)

@pytest.mark.benchmark(group="event_abi_to_log_topic")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_event_abi_to_log_topic(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, eth_utils.event_abi_to_log_topic, abi_element)

@pytest.mark.benchmark(group="event_abi_to_log_topic")
@pytest.mark.parametrize("abi_element", abi_elements)
def test_faster_event_abi_to_log_topic(benchmark: BenchmarkFixture, abi_element: Dict[str, Any]) -> None:
    benchmark(_batch, 100, faster_eth_utils.event_abi_to_log_topic, abi_element)
