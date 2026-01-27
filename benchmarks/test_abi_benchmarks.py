import pytest

from faster_eth_utils.abi import (
    abi_to_signature,
    collapse_if_tuple,
    event_abi_to_log_topic,
    event_signature_to_log_topic,
    filter_abi_by_name,
    filter_abi_by_type,
    function_abi_to_4byte_selector,
    function_signature_to_4byte_selector,
    get_aligned_abi_inputs,
    get_all_event_abis,
    get_all_function_abis,
    get_normalized_abi_inputs,
    get_abi_input_names,
    get_abi_input_types,
    get_abi_output_names,
    get_abi_output_types,
)


@pytest.mark.benchmark
class TestAbiBenchmarks:
    def test_fn_abi_to_4byte_selector(self, benchmark, fixture_abi):
        benchmark(function_abi_to_4byte_selector, fixture_abi)

    def test_abi_to_signature(self, benchmark, fixture_abi):
        benchmark(abi_to_signature, fixture_abi)

    def test_filter_abi_by_name(self, benchmark, fixture_abi):
        benchmark(filter_abi_by_name, fixture_abi, "test_signature")

    def test_filter_abi_by_type(self, benchmark, fixture_abi):
        benchmark(filter_abi_by_type, fixture_abi, "function")

    def test_get_all_event_abis(self, benchmark, fixture_abi):
        benchmark(get_all_event_abis, fixture_abi)

    def test_get_all_function_abis(self, benchmark, fixture_abi):
        benchmark(get_all_function_abis, fixture_abi)

    def test_get_abi_output_types(self, benchmark, fixture_abi):
        benchmark(get_abi_output_types, fixture_abi)

    def test_get_abi_output_names(self, benchmark, fixture_abi):
        benchmark(get_abi_output_names, fixture_abi)

    def test_get_abi_input_types(self, benchmark, fixture_abi):
        benchmark(get_abi_input_types, fixture_abi)

    def test_get_abi_input_names(self, benchmark, fixture_abi):
        benchmark(get_abi_input_names, fixture_abi)

    def test_get_normalized_abi_inputs(self, benchmark, fixture_abi):
        benchmark(get_normalized_abi_inputs, fixture_abi)

    def test_get_aligned_abi_inputs(self, benchmark, fixture_abi):
        benchmark(get_aligned_abi_inputs, fixture_abi)

    def test_collapse_if_tuple(self, benchmark, fixture_abi_component):
        benchmark(collapse_if_tuple, fixture_abi_component)

    def test_event_abi_to_log_topic(self, benchmark, fixture_abi_event):
        benchmark(event_abi_to_log_topic, fixture_abi_event)

    def test_event_signature_to_log_topic(self, benchmark):
        benchmark(event_signature_to_log_topic, "Transfer(address,address,uint256)")
