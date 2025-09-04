#ifndef MYPYC_NATIVE_99c07adba6ff961eaf3e_H
#define MYPYC_NATIVE_99c07adba6ff961eaf3e_H
#include <Python.h>
#include <CPy.h>
#ifndef MYPYC_DECLARED_tuple_T3OOO
#define MYPYC_DECLARED_tuple_T3OOO
typedef struct tuple_T3OOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
} tuple_T3OOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2OO
#define MYPYC_DECLARED_tuple_T2OO
typedef struct tuple_T2OO {
    PyObject *f0;
    PyObject *f1;
} tuple_T2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T4CIOO
#define MYPYC_DECLARED_tuple_T4CIOO
typedef struct tuple_T4CIOO {
    char f0;
    CPyTagged f1;
    PyObject *f2;
    PyObject *f3;
} tuple_T4CIOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T1T2OO
#define MYPYC_DECLARED_tuple_T1T2OO
typedef struct tuple_T1T2OO {
    tuple_T2OO f0;
} tuple_T1T2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2IO
#define MYPYC_DECLARED_tuple_T2IO
typedef struct tuple_T2IO {
    CPyTagged f0;
    PyObject *f1;
} tuple_T2IO;
#endif

#ifndef MYPYC_DECLARED_tuple_T7T2IOT2IOT2IOT2IOT2IOT2IOT2IO
#define MYPYC_DECLARED_tuple_T7T2IOT2IOT2IOT2IOT2IOT2IOT2IO
typedef struct tuple_T7T2IOT2IOT2IOT2IOT2IOT2IOT2IO {
    tuple_T2IO f0;
    tuple_T2IO f1;
    tuple_T2IO f2;
    tuple_T2IO f3;
    tuple_T2IO f4;
    tuple_T2IO f5;
    tuple_T2IO f6;
} tuple_T7T2IOT2IOT2IOT2IOT2IOT2IOT2IO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2II
#define MYPYC_DECLARED_tuple_T2II
typedef struct tuple_T2II {
    CPyTagged f0;
    CPyTagged f1;
} tuple_T2II;
#endif

#ifndef MYPYC_DECLARED_tuple_T0
#define MYPYC_DECLARED_tuple_T0
typedef struct tuple_T0 {
    int empty_struct_error_flag;
} tuple_T0;
#endif

#ifndef MYPYC_DECLARED_tuple_T5OOOOO
#define MYPYC_DECLARED_tuple_T5OOOOO
typedef struct tuple_T5OOOOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
    PyObject *f3;
    PyObject *f4;
} tuple_T5OOOOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T1O
#define MYPYC_DECLARED_tuple_T1O
typedef struct tuple_T1O {
    PyObject *f0;
} tuple_T1O;
#endif

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_formatter;
    CPyTagged _at_index;
    PyObject *_value;
    int32_t ___mypyc_next_label__;
    CPyTagged ___mypyc_temp__0;
    CPyTagged _index;
    PyObject *___mypyc_temp__1;
    CPyTagged ___mypyc_temp__2;
    PyObject *_item;
} faster_eth_utils___applicators___apply_formatter_at_index_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_formatters;
    PyObject *_sequence;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__3;
    CPyTagged ___mypyc_temp__4;
    PyObject *___mypyc_temp__5;
    CPyTagged ___mypyc_temp__6;
    PyObject *_formatter;
    PyObject *_item;
} faster_eth_utils___applicators___apply_formatters_to_sequence_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_formatters;
    PyObject *_value;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__7;
    CPyTagged ___mypyc_temp__8;
    CPyTagged ___mypyc_temp__9;
    PyObject *___mypyc_temp__10;
    PyObject *_key;
    PyObject *_item;
    tuple_T3OOO ___mypyc_temp__11;
    PyObject *_exc;
    PyObject *_new_error_message;
} faster_eth_utils___applicators___apply_formatters_to_dict_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_formatter;
    PyObject *_value;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__12;
    CPyTagged ___mypyc_temp__13;
    PyObject *_item;
} faster_eth_utils___applicators___apply_formatter_to_array_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_key_mappings;
    PyObject *_value;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__14;
    PyObject *___mypyc_temp__15;
    CPyTagged ___mypyc_temp__16;
    CPyTagged ___mypyc_temp__17;
    PyObject *___mypyc_temp__18;
    PyObject *_k;
    PyObject *_v;
    PyObject *_key_conflicts;
    PyObject *___mypyc_temp__19;
    CPyTagged ___mypyc_temp__20;
    CPyTagged ___mypyc_temp__21;
    PyObject *___mypyc_temp__22;
    PyObject *_key;
    PyObject *_item;
} faster_eth_utils___applicators___apply_key_map_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    CPyTagged _wei;
    CPyTagged _kwei;
    CPyTagged _babbage;
    CPyTagged _femtoether;
    CPyTagged _mwei;
    CPyTagged _lovelace;
    CPyTagged _picoether;
    CPyTagged _gwei;
    CPyTagged _shannon;
    CPyTagged _nanoether;
    CPyTagged _nano;
    CPyTagged _szabo;
    CPyTagged _microether;
    CPyTagged _micro;
    CPyTagged _finney;
    CPyTagged _milliether;
    CPyTagged _milli;
    CPyTagged _ether;
    CPyTagged _kether;
    CPyTagged _grand;
    CPyTagged _mether;
    CPyTagged _gether;
    CPyTagged _tether;
} faster_eth_utils___currency___denomsObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_method;
} faster_eth_utils___decorators___combomethodObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_self;
    PyObject *_obj;
    PyObject *_objtype;
    char _None;
    PyObject *__wrapper;
} faster_eth_utils___decorators_____get___3_combomethod_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___decorators____wrapper___3_get___3_combomethod_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    CPyTagged _at_position;
    PyObject *_decorator;
} faster_eth_utils___decorators___return_arg_type_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *___mypyc_env__;
    PyObject *_to_wrap;
    PyObject *_wrapper;
    CPyTagged _at_position;
    PyObject *_decorator;
} faster_eth_utils___decorators___decorator_return_arg_type_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___decorators___decorator_return_arg_type_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___decorators___wrapper_return_arg_type_decorator_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_old_to_new_exceptions;
    PyObject *_old_exceptions;
    PyObject *_decorator;
} faster_eth_utils___decorators___replace_exceptions_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *___mypyc_env__;
    PyObject *_to_wrap;
    PyObject *_wrapped;
    PyObject *_old_to_new_exceptions;
    PyObject *_old_exceptions;
    PyObject *_decorator;
} faster_eth_utils___decorators___decorator_replace_exceptions_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___decorators___decorator_replace_exceptions_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___decorators___wrapped_replace_exceptions_decorator_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_eth_utils___exceptions___ValidationErrorObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_f;
    PyObject *_g;
    PyObject *_combined;
} faster_eth_utils___functional___combine_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___functional___combined_combine_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_callback;
    PyObject *_outer;
} faster_eth_utils___functional___apply_to_return_value_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *___mypyc_env__;
    PyObject *_fn;
    PyObject *_inner;
    PyObject *_callback;
    PyObject *_outer;
} faster_eth_utils___functional___outer_apply_to_return_value_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___functional___outer_apply_to_return_value_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___functional___inner_apply_to_return_value_outer_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_fn;
    PyObject *_to_tuple_wrap;
} faster_eth_utils___functional___to_tuple_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___functional___to_tuple_wrap_to_tuple_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_fn;
    PyObject *_to_list_wrap;
} faster_eth_utils___functional___to_list_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___functional___to_list_wrap_to_list_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_fn;
    PyObject *_to_set_wrap;
} faster_eth_utils___functional___to_set_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___functional___to_set_wrap_to_set_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_fn;
    PyObject *_to_dict_wrap;
} faster_eth_utils___functional___to_dict_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___functional___to_dict_wrap_to_dict_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_units_iter;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__0;
    PyObject *___mypyc_temp__1;
    CPyTagged _amount;
    PyObject *_unit;
    PyObject *___mypyc_temp__2;
    tuple_T3OOO ___mypyc_temp__3;
} faster_eth_utils___humanize____consume_leading_zero_units_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    CPyTagged _seconds;
    int32_t ___mypyc_next_label__;
    CPyTagged _remainder;
    tuple_T7T2IOT2IOT2IOT2IOT2IOT2IOT2IO ___mypyc_temp__4;
    PyObject *___mypyc_temp__5;
    CPyTagged _duration;
    PyObject *_unit;
    CPyTagged _num;
} faster_eth_utils___humanize____humanize_seconds_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_values;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__6;
    PyObject *___mypyc_temp__7;
    CPyTagged _index;
    PyObject *_left;
    PyObject *_right;
} faster_eth_utils___humanize____find_breakpoints_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_values;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__8;
    PyObject *___mypyc_temp__9;
    PyObject *_left;
    PyObject *_right;
    PyObject *_chunk;
} faster_eth_utils___humanize____extract_integer_ranges_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    CPyTagged _chain_id;
    PyObject *_name;
    PyObject *_shortName;
    PyObject *_symbol;
} faster_eth_utils___network___NetworkObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_eth_utils___numeric___ComparableObject;


struct export_table_99c07adba6ff961eaf3e {
    PyObject *(*CPyDef_abi___collapse_if_tuple)(PyObject *cpy_r_abi);
    PyObject *(*CPyDef_abi____abi_to_signature)(PyObject *cpy_r_abi);
    PyObject *(*CPyDef_abi___function_signature_to_4byte_selector)(PyObject *cpy_r_event_signature);
    PyObject *(*CPyDef_abi___function_abi_to_4byte_selector)(PyObject *cpy_r_function_abi);
    PyObject *(*CPyDef_abi___event_signature_to_log_topic)(PyObject *cpy_r_event_signature);
    PyObject *(*CPyDef_abi___event_abi_to_log_topic)(PyObject *cpy_r_event_abi);
    char (*CPyDef_abi_____top_level__)(void);
    PyObject **CPyStatic_address____HEX_ADDRESS_REGEXP;
    char (*CPyDef_address___is_hex_address)(PyObject *cpy_r_value);
    char (*CPyDef_address___is_binary_address)(PyObject *cpy_r_value);
    char (*CPyDef_address___is_address)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_address___to_normalized_address)(PyObject *cpy_r_value);
    char (*CPyDef_address___is_normalized_address)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_address___to_canonical_address)(PyObject *cpy_r_address);
    char (*CPyDef_address___is_canonical_address)(PyObject *cpy_r_address);
    char (*CPyDef_address___is_same_address)(PyObject *cpy_r_left, PyObject *cpy_r_right);
    PyObject *(*CPyDef_address___to_checksum_address)(PyObject *cpy_r_value);
    char (*CPyDef_address___is_checksum_address)(PyObject *cpy_r_value);
    char (*CPyDef_address____is_checksum_formatted)(PyObject *cpy_r_value);
    char (*CPyDef_address___is_checksum_formatted_address)(PyObject *cpy_r_value);
    char (*CPyDef_address_____top_level__)(void);
    PyTypeObject **CPyType_applicators___apply_formatter_at_index_gen;
    PyObject *(*CPyDef_applicators___apply_formatter_at_index_gen)(void);
    PyTypeObject **CPyType_applicators___apply_formatters_to_sequence_gen;
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence_gen)(void);
    PyTypeObject **CPyType_applicators___apply_formatters_to_dict_gen;
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict_gen)(void);
    PyTypeObject **CPyType_applicators___apply_formatter_to_array_gen;
    PyObject *(*CPyDef_applicators___apply_formatter_to_array_gen)(void);
    PyTypeObject **CPyType_applicators___apply_key_map_gen;
    PyObject *(*CPyDef_applicators___apply_key_map_gen)(void);
    PyObject *(*CPyDef_applicators___apply_formatter_at_index_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatter_at_index_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatter_at_index_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatter_at_index_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatter_at_index_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_applicators___apply_formatter_at_index_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatter_at_index)(PyObject *cpy_r_formatter, CPyTagged cpy_r_at_index, PyObject *cpy_r_value);
    PyObject *(*CPyDef_applicators___combine_argument_formatters)(PyObject *cpy_r_formatters);
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatters_to_sequence)(PyObject *cpy_r_formatters, PyObject *cpy_r_sequence);
    PyObject *(*CPyDef_applicators___apply_formatter_if)(PyObject *cpy_r_condition, PyObject *cpy_r_formatter, PyObject *cpy_r_value);
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatters_to_dict)(PyObject *cpy_r_formatters, PyObject *cpy_r_value);
    PyObject *(*CPyDef_applicators___apply_formatter_to_array_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatter_to_array_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatter_to_array_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_formatter_to_array_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatter_to_array_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_applicators___apply_formatter_to_array_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_formatter_to_array)(PyObject *cpy_r_formatter, PyObject *cpy_r_value);
    PyObject *(*CPyDef_applicators___apply_one_of_formatters)(tuple_T1T2OO cpy_r_formatter_condition_pairs, PyObject *cpy_r_value);
    PyObject *(*CPyDef_applicators___apply_key_map_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_key_map_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_key_map_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_applicators___apply_key_map_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_key_map_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_applicators___apply_key_map_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_applicators___apply_key_map)(PyObject *cpy_r_key_mappings, PyObject *cpy_r_value);
    char (*CPyDef_applicators_____top_level__)(void);
    PyObject *(*CPyDef_conversions___to_hex)(PyObject *cpy_r_primitive, PyObject *cpy_r_hexstr, PyObject *cpy_r_text);
    CPyTagged (*CPyDef_conversions___to_int)(PyObject *cpy_r_primitive, PyObject *cpy_r_hexstr, PyObject *cpy_r_text);
    PyObject *(*CPyDef_conversions___to_bytes)(PyObject *cpy_r_primitive, PyObject *cpy_r_hexstr, PyObject *cpy_r_text);
    PyObject *(*CPyDef_conversions___to_text)(PyObject *cpy_r_primitive, PyObject *cpy_r_hexstr, PyObject *cpy_r_text);
    PyObject *(*CPyDef_conversions___text_if_str)(PyObject *cpy_r_to_type, PyObject *cpy_r_text_or_primitive);
    PyObject *(*CPyDef_conversions___hexstr_if_str)(PyObject *cpy_r_to_type, PyObject *cpy_r_hexstr_or_primitive);
    char (*CPyDef_conversions_____top_level__)(void);
    PyObject *(*CPyDef_crypto___keccak)(PyObject *cpy_r_primitive, PyObject *cpy_r_hexstr, PyObject *cpy_r_text);
    char (*CPyDef_crypto_____top_level__)(void);
    CPyTagged *CPyStatic_currency___denoms___wei;
    CPyTagged *CPyStatic_currency___denoms___kwei;
    CPyTagged *CPyStatic_currency___denoms___babbage;
    CPyTagged *CPyStatic_currency___denoms___femtoether;
    CPyTagged *CPyStatic_currency___denoms___mwei;
    CPyTagged *CPyStatic_currency___denoms___lovelace;
    CPyTagged *CPyStatic_currency___denoms___picoether;
    CPyTagged *CPyStatic_currency___denoms___gwei;
    CPyTagged *CPyStatic_currency___denoms___shannon;
    CPyTagged *CPyStatic_currency___denoms___nanoether;
    CPyTagged *CPyStatic_currency___denoms___nano;
    CPyTagged *CPyStatic_currency___denoms___szabo;
    CPyTagged *CPyStatic_currency___denoms___microether;
    CPyTagged *CPyStatic_currency___denoms___micro;
    CPyTagged *CPyStatic_currency___denoms___finney;
    CPyTagged *CPyStatic_currency___denoms___milliether;
    CPyTagged *CPyStatic_currency___denoms___milli;
    CPyTagged *CPyStatic_currency___denoms___ether;
    CPyTagged *CPyStatic_currency___denoms___kether;
    CPyTagged *CPyStatic_currency___denoms___grand;
    CPyTagged *CPyStatic_currency___denoms___mether;
    CPyTagged *CPyStatic_currency___denoms___gether;
    CPyTagged *CPyStatic_currency___denoms___tether;
    PyTypeObject **CPyType_currency___denoms;
    PyObject *(*CPyDef_currency___denoms)(void);
    char (*CPyDef_currency___denoms_____mypyc_defaults_setup)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_currency___from_wei)(CPyTagged cpy_r_number, PyObject *cpy_r_unit);
    CPyTagged (*CPyDef_currency___to_wei)(PyObject *cpy_r_number, PyObject *cpy_r_unit);
    char (*CPyDef_currency_____top_level__)(void);
    PyObject *(*CPyDef_debug___pip_freeze)(void);
    PyObject *(*CPyDef_debug___python_version)(void);
    PyObject *(*CPyDef_debug___platform_info)(void);
    PyObject *(*CPyDef_debug___get_environment_summary)(void);
    char (*CPyDef_debug_____top_level__)(void);
    PyTypeObject **CPyType_decorators___combomethod;
    PyObject *(*CPyDef_decorators___combomethod)(PyObject *cpy_r_method);
    PyTypeObject **CPyType_decorators_____get___3_combomethod_env;
    PyObject *(*CPyDef_decorators_____get___3_combomethod_env)(void);
    PyTypeObject **CPyType_decorators____wrapper___3_get___3_combomethod_obj;
    PyObject *(*CPyDef_decorators____wrapper___3_get___3_combomethod_obj)(void);
    PyTypeObject **CPyType_decorators___return_arg_type_env;
    PyObject *(*CPyDef_decorators___return_arg_type_env)(void);
    PyTypeObject **CPyType_decorators___decorator_return_arg_type_env;
    PyObject *(*CPyDef_decorators___decorator_return_arg_type_env)(void);
    PyTypeObject **CPyType_decorators___decorator_return_arg_type_obj;
    PyObject *(*CPyDef_decorators___decorator_return_arg_type_obj)(void);
    PyTypeObject **CPyType_decorators___wrapper_return_arg_type_decorator_obj;
    PyObject *(*CPyDef_decorators___wrapper_return_arg_type_decorator_obj)(void);
    PyTypeObject **CPyType_decorators___replace_exceptions_env;
    PyObject *(*CPyDef_decorators___replace_exceptions_env)(void);
    PyTypeObject **CPyType_decorators___decorator_replace_exceptions_env;
    PyObject *(*CPyDef_decorators___decorator_replace_exceptions_env)(void);
    PyTypeObject **CPyType_decorators___decorator_replace_exceptions_obj;
    PyObject *(*CPyDef_decorators___decorator_replace_exceptions_obj)(void);
    PyTypeObject **CPyType_decorators___wrapped_replace_exceptions_decorator_obj;
    PyObject *(*CPyDef_decorators___wrapped_replace_exceptions_decorator_obj)(void);
    char (*CPyDef_decorators___combomethod_____init__)(PyObject *cpy_r_self, PyObject *cpy_r_method);
    PyObject *(*CPyDef_decorators____wrapper___3_get___3_combomethod_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_decorators____wrapper___3_get___3_combomethod_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_decorators___combomethod_____get__)(PyObject *cpy_r_self, PyObject *cpy_r_obj, PyObject *cpy_r_objtype);
    PyObject *(*CPyDef_decorators___wrapper_return_arg_type_decorator_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_decorators___wrapper_return_arg_type_decorator_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_decorators___decorator_return_arg_type_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_decorators___decorator_return_arg_type_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_to_wrap);
    PyObject *(*CPyDef_decorators___return_arg_type)(CPyTagged cpy_r_at_position);
    PyObject *(*CPyDef_decorators___wrapped_replace_exceptions_decorator_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_decorators___wrapped_replace_exceptions_decorator_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_decorators___decorator_replace_exceptions_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_decorators___decorator_replace_exceptions_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_to_wrap);
    PyObject *(*CPyDef_decorators___replace_exceptions)(PyObject *cpy_r_old_to_new_exceptions);
    char (*CPyDef_decorators_____top_level__)(void);
    PyObject *(*CPyDef_encoding___int_to_big_endian)(CPyTagged cpy_r_value);
    CPyTagged (*CPyDef_encoding___big_endian_to_int)(PyObject *cpy_r_value);
    char (*CPyDef_encoding_____top_level__)(void);
    PyTypeObject **CPyType_exceptions___ValidationError;
    char (*CPyDef_exceptions_____top_level__)(void);
    PyTypeObject **CPyType_functional___combine_env;
    PyObject *(*CPyDef_functional___combine_env)(void);
    PyTypeObject **CPyType_functional___combined_combine_obj;
    PyObject *(*CPyDef_functional___combined_combine_obj)(void);
    PyTypeObject **CPyType_functional___apply_to_return_value_env;
    PyObject *(*CPyDef_functional___apply_to_return_value_env)(void);
    PyTypeObject **CPyType_functional___outer_apply_to_return_value_env;
    PyObject *(*CPyDef_functional___outer_apply_to_return_value_env)(void);
    PyTypeObject **CPyType_functional___outer_apply_to_return_value_obj;
    PyObject *(*CPyDef_functional___outer_apply_to_return_value_obj)(void);
    PyTypeObject **CPyType_functional___inner_apply_to_return_value_outer_obj;
    PyObject *(*CPyDef_functional___inner_apply_to_return_value_outer_obj)(void);
    PyTypeObject **CPyType_functional___to_tuple_env;
    PyObject *(*CPyDef_functional___to_tuple_env)(void);
    PyTypeObject **CPyType_functional___to_tuple_wrap_to_tuple_obj;
    PyObject *(*CPyDef_functional___to_tuple_wrap_to_tuple_obj)(void);
    PyTypeObject **CPyType_functional___to_list_env;
    PyObject *(*CPyDef_functional___to_list_env)(void);
    PyTypeObject **CPyType_functional___to_list_wrap_to_list_obj;
    PyObject *(*CPyDef_functional___to_list_wrap_to_list_obj)(void);
    PyTypeObject **CPyType_functional___to_set_env;
    PyObject *(*CPyDef_functional___to_set_env)(void);
    PyTypeObject **CPyType_functional___to_set_wrap_to_set_obj;
    PyObject *(*CPyDef_functional___to_set_wrap_to_set_obj)(void);
    PyTypeObject **CPyType_functional___to_dict_env;
    PyObject *(*CPyDef_functional___to_dict_env)(void);
    PyTypeObject **CPyType_functional___to_dict_wrap_to_dict_obj;
    PyObject *(*CPyDef_functional___to_dict_wrap_to_dict_obj)(void);
    PyObject *(*CPyDef_functional___identity)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_functional___combined_combine_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_functional___combined_combine_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_x);
    PyObject *(*CPyDef_functional___combine)(PyObject *cpy_r_f, PyObject *cpy_r_g);
    PyObject *(*CPyDef_functional___inner_apply_to_return_value_outer_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_functional___inner_apply_to_return_value_outer_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_functional___outer_apply_to_return_value_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_functional___outer_apply_to_return_value_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_fn);
    PyObject *(*CPyDef_functional___apply_to_return_value)(PyObject *cpy_r_callback);
    PyObject *(*CPyDef_functional___to_tuple_wrap_to_tuple_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_functional___to_tuple_wrap_to_tuple_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_functional___to_tuple)(PyObject *cpy_r_fn);
    PyObject *(*CPyDef_functional___to_list_wrap_to_list_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_functional___to_list_wrap_to_list_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_functional___to_list)(PyObject *cpy_r_fn);
    PyObject *(*CPyDef_functional___to_set_wrap_to_set_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_functional___to_set_wrap_to_set_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_functional___to_set)(PyObject *cpy_r_fn);
    PyObject *(*CPyDef_functional___to_dict_wrap_to_dict_obj_____get__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
    PyObject *(*CPyDef_functional___to_dict_wrap_to_dict_obj_____call__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_functional___to_dict)(PyObject *cpy_r_fn);
    char (*CPyDef_functional_____top_level__)(void);
    PyObject **CPyStatic_hexadecimal____HEX_REGEXP;
    PyObject *(*CPyDef_hexadecimal___decode_hex)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_hexadecimal___encode_hex)(PyObject *cpy_r_value);
    char (*CPyDef_hexadecimal___is_0x_prefixed)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_hexadecimal___remove_0x_prefix)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_hexadecimal___add_0x_prefix)(PyObject *cpy_r_value);
    char (*CPyDef_hexadecimal___is_hexstr)(PyObject *cpy_r_value);
    char (*CPyDef_hexadecimal___is_hex)(PyObject *cpy_r_value);
    char (*CPyDef_hexadecimal_____top_level__)(void);
    tuple_T7T2IOT2IOT2IOT2IOT2IOT2IOT2IO *CPyStatic_humanize___UNITS;
    PyTypeObject **CPyType_humanize____consume_leading_zero_units_gen;
    PyObject *(*CPyDef_humanize____consume_leading_zero_units_gen)(void);
    PyTypeObject **CPyType_humanize____humanize_seconds_gen;
    PyObject *(*CPyDef_humanize____humanize_seconds_gen)(void);
    PyTypeObject **CPyType_humanize____find_breakpoints_gen;
    PyObject *(*CPyDef_humanize____find_breakpoints_gen)(void);
    PyTypeObject **CPyType_humanize____extract_integer_ranges_gen;
    PyObject *(*CPyDef_humanize____extract_integer_ranges_gen)(void);
    PyObject *(*CPyDef_humanize___humanize_seconds)(PyObject *cpy_r_seconds);
    PyObject *(*CPyDef_humanize____consume_leading_zero_units_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____consume_leading_zero_units_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____consume_leading_zero_units_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____consume_leading_zero_units_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____consume_leading_zero_units_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_humanize____consume_leading_zero_units_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____consume_leading_zero_units)(PyObject *cpy_r_units_iter);
    PyObject *(*CPyDef_humanize____humanize_seconds_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____humanize_seconds_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____humanize_seconds_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____humanize_seconds_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____humanize_seconds_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_humanize____humanize_seconds_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____humanize_seconds)(CPyTagged cpy_r_seconds);
    PyObject *(*CPyDef_humanize___humanize_bytes)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_humanize___humanize_hash)(PyObject *cpy_r_value);
    PyObject *(*CPyDef_humanize___humanize_ipfs_uri)(PyObject *cpy_r_uri);
    char (*CPyDef_humanize___is_ipfs_uri)(PyObject *cpy_r_value);
    char (*CPyDef_humanize____is_CIDv0_ipfs_hash)(PyObject *cpy_r_ipfs_hash);
    PyObject *(*CPyDef_humanize____find_breakpoints_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____find_breakpoints_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____find_breakpoints_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____find_breakpoints_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____find_breakpoints_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_humanize____find_breakpoints_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____find_breakpoints)(PyObject *cpy_r_values);
    PyObject *(*CPyDef_humanize____extract_integer_ranges_gen_____mypyc_generator_helper__)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____extract_integer_ranges_gen_____next__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____extract_integer_ranges_gen___send)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
    PyObject *(*CPyDef_humanize____extract_integer_ranges_gen_____iter__)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____extract_integer_ranges_gen___throw)(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
    PyObject *(*CPyDef_humanize____extract_integer_ranges_gen___close)(PyObject *cpy_r___mypyc_self__);
    PyObject *(*CPyDef_humanize____extract_integer_ranges)(PyObject *cpy_r_values);
    PyObject *(*CPyDef_humanize____humanize_range)(tuple_T2II cpy_r_bounds);
    PyObject *(*CPyDef_humanize___humanize_integer_sequence)(PyObject *cpy_r_values_iter);
    PyObject *(*CPyDef_humanize___humanize_wei)(CPyTagged cpy_r_number);
    char (*CPyDef_humanize_____top_level__)(void);
    PyObject *(*CPyDef_module_loading___import_string)(PyObject *cpy_r_dotted_path);
    char (*CPyDef_module_loading_____top_level__)(void);
    PyObject **CPyStatic_network___FASTER_ETH_UTILS_FOLDER;
    PyTypeObject **CPyType_network___Network;
    PyObject *(*CPyDef_network___Network)(PyObject *cpy_r_args, PyObject *cpy_r_kwargs);
    PyObject *(*CPyDef_network___initialize_network_objects)(void);
    PyObject *(*CPyDef_network___network_from_chain_id)(CPyTagged cpy_r_chain_id);
    PyObject *(*CPyDef_network___name_from_chain_id)(CPyTagged cpy_r_chain_id);
    PyObject *(*CPyDef_network___short_name_from_chain_id)(CPyTagged cpy_r_chain_id);
    char (*CPyDef_network_____top_level__)(void);
    PyTypeObject **CPyType_numeric___Comparable;
    PyObject *(*CPyDef_numeric___Comparable)(void);
    PyObject *(*CPyDef_numeric___Comparable_____lt__)(PyObject *cpy_r_self, PyObject *cpy_r_other);
    PyObject *(*CPyDef_numeric___Comparable_____gt__)(PyObject *cpy_r_self, PyObject *cpy_r_other);
    PyObject *(*CPyDef_numeric___clamp)(PyObject *cpy_r_lower_bound, PyObject *cpy_r_upper_bound, PyObject *cpy_r_value);
    char (*CPyDef_numeric_____top_level__)(void);
    char (*CPyDef_toolz_____top_level__)(void);
    char (*CPyDef_types___is_integer)(PyObject *cpy_r_value);
    char (*CPyDef_types___is_bytes)(PyObject *cpy_r_value);
    char (*CPyDef_types___is_text)(PyObject *cpy_r_value);
    char (*CPyDef_types___is_string)(PyObject *cpy_r_value);
    char (*CPyDef_types___is_boolean)(PyObject *cpy_r_value);
    char (*CPyDef_types___is_dict)(PyObject *cpy_r_obj);
    char (*CPyDef_types___is_list_like)(PyObject *cpy_r_obj);
    char (*CPyDef_types___is_list)(PyObject *cpy_r_obj);
    char (*CPyDef_types___is_tuple)(PyObject *cpy_r_obj);
    char (*CPyDef_types___is_null)(PyObject *cpy_r_obj);
    char (*CPyDef_types___is_number)(PyObject *cpy_r_obj);
    char (*CPyDef_types_____top_level__)(void);
    char (*CPyDef_units_____top_level__)(void);
};
#endif
