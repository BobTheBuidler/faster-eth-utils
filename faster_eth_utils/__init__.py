from importlib import import_module
from importlib.metadata import (
    version as _version,
)
from typing import TYPE_CHECKING

__version__ = _version("faster-eth-utils")

if TYPE_CHECKING:
    from .abi import (
        abi_to_signature,
        collapse_if_tuple,
        event_abi_to_log_topic,
        event_signature_to_log_topic,
        filter_abi_by_name,
        filter_abi_by_type,
        function_abi_to_4byte_selector,
        function_signature_to_4byte_selector,
        get_abi_input_names,
        get_abi_input_types,
        get_abi_output_names,
        get_abi_output_types,
        get_aligned_abi_inputs,
        get_all_event_abis,
        get_all_function_abis,
        get_normalized_abi_inputs,
    )
    from .address import (
        is_address,
        is_binary_address,
        is_canonical_address,
        is_checksum_address,
        is_checksum_formatted_address,
        is_hex_address,
        is_normalized_address,
        is_same_address,
        to_canonical_address,
        to_checksum_address,
        to_normalized_address,
    )
    from .applicators import (
        apply_formatter_at_index,
        apply_formatter_if,
        apply_formatter_to_array,
        apply_formatters_to_dict,
        apply_formatters_to_sequence,
        apply_key_map,
        apply_one_of_formatters,
        combine_argument_formatters,
    )
    from .conversions import (
        hexstr_if_str,
        text_if_str,
        to_bytes,
        to_hex,
        to_int,
        to_text,
    )
    from .crypto import (
        keccak,
    )
    from .currency import (
        denoms,
        from_wei,
        from_wei_decimals,
        to_wei,
        to_wei_decimals,
    )
    from .decorators import (
        combomethod,
        replace_exceptions,
    )
    from .encoding import (
        big_endian_to_int,
        int_to_big_endian,
    )
    from .exceptions import (
        ValidationError,
    )
    from .functional import (
        apply_to_return_value,
        flatten_return,
        reversed_return,
        sort_return,
        to_dict,
        to_list,
        to_ordered_dict,
        to_set,
        to_tuple,
    )
    from .hexadecimal import (
        add_0x_prefix,
        decode_hex,
        encode_hex,
        is_0x_prefixed,
        is_hex,
        is_hexstr,
        remove_0x_prefix,
    )
    from .humanize import (
        humanize_bytes,
        humanize_hash,
        humanize_hexstr,
        humanize_integer_sequence,
        humanize_ipfs_uri,
        humanize_seconds,
        humanize_wei,
    )
    from .logging import (
        DEBUG2_LEVEL_NUM,
        ExtendedDebugLogger,
        HasExtendedDebugLogger,
        HasExtendedDebugLoggerMeta,
        HasLogger,
        HasLoggerMeta,
        get_extended_debug_logger,
        get_logger,
        setup_DEBUG2_logging,
    )
    from .module_loading import (
        import_string,
    )
    from .network import (
        Network,
        name_from_chain_id,
        network_from_chain_id,
        short_name_from_chain_id,
    )
    from .numeric import (
        clamp,
    )
    from .pydantic import (
        CamelModel,
    )
    from .types import (
        is_boolean,
        is_bytes,
        is_dict,
        is_integer,
        is_list,
        is_list_like,
        is_null,
        is_number,
        is_string,
        is_text,
        is_tuple,
    )

_LAZY_IMPORTS = {
    "abi_to_signature": "faster_eth_utils.abi",
    "collapse_if_tuple": "faster_eth_utils.abi",
    "event_abi_to_log_topic": "faster_eth_utils.abi",
    "event_signature_to_log_topic": "faster_eth_utils.abi",
    "filter_abi_by_name": "faster_eth_utils.abi",
    "filter_abi_by_type": "faster_eth_utils.abi",
    "function_abi_to_4byte_selector": "faster_eth_utils.abi",
    "function_signature_to_4byte_selector": "faster_eth_utils.abi",
    "get_abi_input_names": "faster_eth_utils.abi",
    "get_abi_input_types": "faster_eth_utils.abi",
    "get_abi_output_names": "faster_eth_utils.abi",
    "get_abi_output_types": "faster_eth_utils.abi",
    "get_aligned_abi_inputs": "faster_eth_utils.abi",
    "get_all_event_abis": "faster_eth_utils.abi",
    "get_all_function_abis": "faster_eth_utils.abi",
    "get_normalized_abi_inputs": "faster_eth_utils.abi",
    "is_address": "faster_eth_utils.address",
    "is_binary_address": "faster_eth_utils.address",
    "is_canonical_address": "faster_eth_utils.address",
    "is_checksum_address": "faster_eth_utils.address",
    "is_checksum_formatted_address": "faster_eth_utils.address",
    "is_hex_address": "faster_eth_utils.address",
    "is_normalized_address": "faster_eth_utils.address",
    "is_same_address": "faster_eth_utils.address",
    "to_canonical_address": "faster_eth_utils.address",
    "to_checksum_address": "faster_eth_utils.address",
    "to_normalized_address": "faster_eth_utils.address",
    "apply_formatter_at_index": "faster_eth_utils.applicators",
    "apply_formatter_if": "faster_eth_utils.applicators",
    "apply_formatter_to_array": "faster_eth_utils.applicators",
    "apply_formatters_to_dict": "faster_eth_utils.applicators",
    "apply_formatters_to_sequence": "faster_eth_utils.applicators",
    "apply_key_map": "faster_eth_utils.applicators",
    "apply_one_of_formatters": "faster_eth_utils.applicators",
    "combine_argument_formatters": "faster_eth_utils.applicators",
    "hexstr_if_str": "faster_eth_utils.conversions",
    "text_if_str": "faster_eth_utils.conversions",
    "to_bytes": "faster_eth_utils.conversions",
    "to_hex": "faster_eth_utils.conversions",
    "to_int": "faster_eth_utils.conversions",
    "to_text": "faster_eth_utils.conversions",
    "keccak": "faster_eth_utils.crypto",
    "denoms": "faster_eth_utils.currency",
    "from_wei": "faster_eth_utils.currency",
    "from_wei_decimals": "faster_eth_utils.currency",
    "to_wei": "faster_eth_utils.currency",
    "to_wei_decimals": "faster_eth_utils.currency",
    "combomethod": "faster_eth_utils.decorators",
    "replace_exceptions": "faster_eth_utils.decorators",
    "big_endian_to_int": "faster_eth_utils.encoding",
    "int_to_big_endian": "faster_eth_utils.encoding",
    "ValidationError": "faster_eth_utils.exceptions",
    "apply_to_return_value": "faster_eth_utils.functional",
    "flatten_return": "faster_eth_utils.functional",
    "reversed_return": "faster_eth_utils.functional",
    "sort_return": "faster_eth_utils.functional",
    "to_dict": "faster_eth_utils.functional",
    "to_list": "faster_eth_utils.functional",
    "to_ordered_dict": "faster_eth_utils.functional",
    "to_set": "faster_eth_utils.functional",
    "to_tuple": "faster_eth_utils.functional",
    "add_0x_prefix": "faster_eth_utils.hexadecimal",
    "decode_hex": "faster_eth_utils.hexadecimal",
    "encode_hex": "faster_eth_utils.hexadecimal",
    "is_0x_prefixed": "faster_eth_utils.hexadecimal",
    "is_hex": "faster_eth_utils.hexadecimal",
    "is_hexstr": "faster_eth_utils.hexadecimal",
    "remove_0x_prefix": "faster_eth_utils.hexadecimal",
    "humanize_bytes": "faster_eth_utils.humanize",
    "humanize_hash": "faster_eth_utils.humanize",
    "humanize_hexstr": "faster_eth_utils.humanize",
    "humanize_integer_sequence": "faster_eth_utils.humanize",
    "humanize_ipfs_uri": "faster_eth_utils.humanize",
    "humanize_seconds": "faster_eth_utils.humanize",
    "humanize_wei": "faster_eth_utils.humanize",
    "DEBUG2_LEVEL_NUM": "faster_eth_utils.logging",
    "ExtendedDebugLogger": "faster_eth_utils.logging",
    "HasExtendedDebugLogger": "faster_eth_utils.logging",
    "HasExtendedDebugLoggerMeta": "faster_eth_utils.logging",
    "HasLogger": "faster_eth_utils.logging",
    "HasLoggerMeta": "faster_eth_utils.logging",
    "get_extended_debug_logger": "faster_eth_utils.logging",
    "get_logger": "faster_eth_utils.logging",
    "setup_DEBUG2_logging": "faster_eth_utils.logging",
    "import_string": "faster_eth_utils.module_loading",
    "Network": "faster_eth_utils.network",
    "name_from_chain_id": "faster_eth_utils.network",
    "network_from_chain_id": "faster_eth_utils.network",
    "short_name_from_chain_id": "faster_eth_utils.network",
    "clamp": "faster_eth_utils.numeric",
    "CamelModel": "faster_eth_utils.pydantic",
    "is_boolean": "faster_eth_utils.types",
    "is_bytes": "faster_eth_utils.types",
    "is_dict": "faster_eth_utils.types",
    "is_integer": "faster_eth_utils.types",
    "is_list": "faster_eth_utils.types",
    "is_list_like": "faster_eth_utils.types",
    "is_null": "faster_eth_utils.types",
    "is_number": "faster_eth_utils.types",
    "is_string": "faster_eth_utils.types",
    "is_text": "faster_eth_utils.types",
    "is_tuple": "faster_eth_utils.types",
}

__all__ = ["__version__", *_LAZY_IMPORTS]


def __getattr__(name: str):
    module_name = _LAZY_IMPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(module_name)
    value = getattr(module, name)
    globals()[name] = value
    return value


def __dir__():
    return sorted({*globals(), *_LAZY_IMPORTS})
