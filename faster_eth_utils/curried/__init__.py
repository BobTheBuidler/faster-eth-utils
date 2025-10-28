from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Generator,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import TypeGuard

from faster_eth_utils import (
    CamelModel,
    ExtendedDebugLogger,
    HasExtendedDebugLogger,
    HasExtendedDebugLoggerMeta,
    HasLogger,
    HasLoggerMeta,
    Network,
    ValidationError,
    abi_to_signature,
    add_0x_prefix,
    apply_formatter_at_index,
    apply_formatter_if as non_curried_apply_formatter_if,
    apply_formatter_to_array,
    apply_formatters_to_dict as non_curried_apply_formatters_to_dict,
    apply_formatters_to_sequence,
    apply_key_map,
    apply_one_of_formatters as non_curried_apply_one_of_formatters,
    apply_to_return_value,
    big_endian_to_int,
    clamp,
    collapse_if_tuple,
    combine_argument_formatters,
    combomethod,
    decode_hex,
    denoms,
    encode_hex,
    event_abi_to_log_topic,
    event_signature_to_log_topic,
    filter_abi_by_name,
    filter_abi_by_type,
    flatten_return,
    from_wei,
    from_wei_decimals,
    function_abi_to_4byte_selector,
    function_signature_to_4byte_selector,
    get_abi_input_names,
    get_abi_input_types,
    get_abi_output_names,
    get_abi_output_types,
    get_aligned_abi_inputs,
    get_all_event_abis,
    get_all_function_abis,
    get_extended_debug_logger,
    get_logger,
    get_normalized_abi_inputs,
    hexstr_if_str as non_curried_hexstr_if_str,
    humanize_bytes,
    humanize_hash,
    humanize_hexstr,
    humanize_integer_sequence,
    humanize_ipfs_uri,
    humanize_seconds,
    humanize_wei,
    import_string,
    int_to_big_endian,
    is_0x_prefixed,
    is_address,
    is_binary_address,
    is_boolean,
    is_bytes,
    is_canonical_address,
    is_checksum_address,
    is_checksum_formatted_address,
    is_dict,
    is_hex,
    is_hex_address,
    is_hexstr,
    is_integer,
    is_list,
    is_list_like,
    is_normalized_address,
    is_null,
    is_number,
    is_same_address,
    is_string,
    is_text,
    is_tuple,
    keccak,
    name_from_chain_id,
    network_from_chain_id,
    remove_0x_prefix,
    replace_exceptions,
    reversed_return,
    setup_DEBUG2_logging,
    short_name_from_chain_id,
    sort_return,
    text_if_str as non_curried_text_if_str,
    to_bytes,
    to_canonical_address,
    to_checksum_address,
    to_dict,
    to_hex,
    to_int,
    to_list,
    to_normalized_address,
    to_ordered_dict,
    to_set,
    to_text,
    to_tuple,
    to_wei,
    to_wei_decimals,
)
from faster_eth_utils.toolz import (
    curry,
)

if TYPE_CHECKING:
    from _typeshed import SupportsBool


TArg = TypeVar("TArg")
TOther = TypeVar("TOther")
TReturn = TypeVar("TReturn")
TValue = TypeVar("TValue")


@overload
def apply_formatter_if(
    condition: Callable[[TArg], TypeGuard[TOther]],
) -> Callable[[Callable[[TOther], TReturn]], Callable[[TArg], Union[TReturn, TArg]]]:
    ...

@overload
def apply_formatter_if(
    condition: Callable[[TArg], TypeGuard[TOther]], formatter: Callable[[TOther], TReturn]
) -> Callable[[TArg], Union[TReturn, TArg]]:
    ...

@overload
def apply_formatter_if(
    condition: Callable[[TArg], TypeGuard[TOther]], formatter: Callable[[TOther], TReturn], value: TArg
) -> Union[TReturn, TArg]:
    ...

@overload
def apply_formatter_if(
    condition: Callable[[TArg], bool], formatter: Callable[[TArg], TReturn], value: TArg
) -> Union[TReturn, TArg]:
    ...

def apply_formatter_if(  # type: ignore
    condition: Union[Callable[[TArg], TypeGuard[TOther]], Callable[[TArg], bool]],
    formatter: Optional[Union[Callable[[TOther], TReturn], Callable[[TArg], TReturn]]] = None,
    value: Optional[TArg] = None,
) -> Union[
    Callable[[Callable[[TOther], TReturn]], Callable[[TArg], Union[TReturn, TArg]]],
    Callable[[TArg], Union[TReturn, TArg]],
    TReturn,
    TArg,
]:
    pass


@overload
def apply_one_of_formatters(
    formatter_condition_pairs: Sequence[
        Tuple[Callable[[TArg], "SupportsBool"], Callable[[TArg], TReturn]]
    ],
) -> Callable[[TArg], TReturn]: ...


@overload
def apply_one_of_formatters(
    formatter_condition_pairs: Sequence[
        Tuple[Callable[[TArg], "SupportsBool"], Callable[[TArg], TReturn]]
    ],
    value: TArg,
) -> TReturn: ...


# This is just a stub to appease mypy, it gets overwritten later
def apply_one_of_formatters(
    formatter_condition_pairs: Sequence[
        Tuple[Callable[[TArg], "SupportsBool"], Callable[[TArg], TReturn]]
    ],
    value: Optional[TArg] = None,
) -> TReturn: ...


@overload
def hexstr_if_str(
    to_type: Callable[..., TReturn],
) -> Callable[[Union[bytes, int, str]], TReturn]: ...


@overload
def hexstr_if_str(
    to_type: Callable[..., TReturn], to_format: Union[bytes, int, str]
) -> TReturn: ...


# This is just a stub to appease mypy, it gets overwritten later
def hexstr_if_str(  # type: ignore
    to_type: Callable[..., TReturn], to_format: Optional[Union[bytes, int, str]] = None
) -> TReturn: ...


@overload
def text_if_str(
    to_type: Callable[..., TReturn],
) -> Callable[[Union[bytes, int, str]], TReturn]: ...


@overload
def text_if_str(
    to_type: Callable[..., TReturn], text_or_primitive: Union[bytes, int, str]
) -> TReturn: ...


# This is just a stub to appease mypy, it gets overwritten later
def text_if_str(  # type: ignore
    to_type: Callable[..., TReturn],
    text_or_primitive: Optional[Union[bytes, int, str]] = None,
) -> TReturn: ...


@overload
def apply_formatters_to_dict(
    formatters: Dict[Any, Any], unaliased: bool = False
) -> Callable[[Union[Dict[Any, Any], CamelModel]], Dict[Any, Any]]:
    ...


@overload
def apply_formatters_to_dict(
    formatters: Dict[Any, Any], value: Union[Dict[Any, Any], CamelModel], unaliased: bool = False
) -> Dict[Any, Any]:
    ...


# This is just a stub to appease mypy, it gets overwritten later
def apply_formatters_to_dict(
    formatters: Dict[Any, Any],
    value: Optional[Union[Dict[Any, Any], CamelModel]] = None,
    unaliased: bool = False,
) -> Dict[Any, Any]: ...


apply_formatter_at_index = curry(apply_formatter_at_index)
apply_formatter_if = curry(non_curried_apply_formatter_if)  # noqa: F811
apply_formatter_to_array = curry(apply_formatter_to_array)
apply_formatters_to_dict = curry(non_curried_apply_formatters_to_dict)  # noqa: F811
apply_formatters_to_sequence = curry(apply_formatters_to_sequence)
apply_key_map = curry(apply_key_map)
apply_one_of_formatters = curry(non_curried_apply_one_of_formatters)  # noqa: F811
filter_abi_by_name = curry(filter_abi_by_name)
filter_abi_by_type = curry(filter_abi_by_type)
flatten_return = curry(flatten_return)
from_wei = curry(from_wei)
from_wei_decimals = curry(from_wei_decimals)
get_aligned_abi_inputs = curry(get_aligned_abi_inputs)
get_logger = curry(get_logger)
get_normalized_abi_inputs = curry(get_normalized_abi_inputs)
hexstr_if_str = curry(non_curried_hexstr_if_str)  # noqa: F811
is_same_address = curry(is_same_address)
sort_return = curry(sort_return)
text_if_str = curry(non_curried_text_if_str)  # noqa: F811
to_ordered_dict = curry(to_ordered_dict)
to_wei = curry(to_wei)
to_wei_decimals = curry(to_wei_decimals)
clamp = curry(clamp)

# Delete any methods and classes that are not intended to be importable from
# `eth_utils.curried`. We do this approach instead of __all__ because this approach
# actually prevents importing the wrong thing, while __all__ only affects
# `from eth_utils.curried import *`
del Any
del Callable
del Dict
del Generator
del Optional
del Sequence
del TReturn
del TValue
del Tuple
del TypeGuard
del TypeVar
del Union
del curry
del non_curried_apply_formatter_if
del non_curried_apply_one_of_formatters
del non_curried_apply_formatters_to_dict
del non_curried_hexstr_if_str
del non_curried_text_if_str
del overload
