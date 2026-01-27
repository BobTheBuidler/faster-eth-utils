# ABI

## Type checking and normalization

| `fn_abi_to_4byte_selector` | `abi_to_signature` | `filter_abi_by_name` | `filter_abi_by_type` | `get_all_event_abis` | `get_all_function_abis` | `get_abi_output_types` | `get_abi_output_names` | `get_abi_input_types` | `get_abi_input_names` | `get_abi_inputs` | `get_normalized_abi_inputs` | `get_aligned_abi_inputs` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `4.58 us` | `8.68 us` | `6.51 us` | `8.16 us` | `10.86 us` | `10.62 us` | `13.15 us` | `15.51 us` | `2.78 us` | `3.43 us` | `2.95 us` | `22.40 us` | `23.54 us` |

## ABI modifications

| `collapse_if_tuple` | `normalize_abi` | `normalize_abi_input` | `normalize_abi_parameter` | `normalize_event_input_types` | `normalize_event_abi` | `normalize_function_input_types` | `normalize_function_abi` | `normalize_abi_type` | `normalize_abi_type_recursive` | `merge_args_and_kwargs` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `18.40 us` | `82.97 us` | `58.66 us` | `37.37 us` | `37.16 us` | `35.74 us` | `38.38 us` | `35.44 us` | `7.41 us` | `11.54 us` | `1.89 us` |

## Signature to topic or selector

| `function_signature_to_4byte_selector` | `event_abi_to_log_topic` | `event_signature_to_log_topic` |
| --- | --- | --- |
| `0.55 us` | `0.63 us` | `0.47 us` |
