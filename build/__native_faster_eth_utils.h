#ifndef MYPYC_NATIVE_faster_eth_utils_H
#define MYPYC_NATIVE_faster_eth_utils_H
#include <Python.h>
#include <CPy.h>
#ifndef MYPYC_DECLARED_tuple_T2OO
#define MYPYC_DECLARED_tuple_T2OO
typedef struct tuple_T2OO {
    PyObject *f0;
    PyObject *f1;
} tuple_T2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T6OOOOOO
#define MYPYC_DECLARED_tuple_T6OOOOOO
typedef struct tuple_T6OOOOOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
    PyObject *f3;
    PyObject *f4;
    PyObject *f5;
} tuple_T6OOOOOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T3OOO
#define MYPYC_DECLARED_tuple_T3OOO
typedef struct tuple_T3OOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
} tuple_T3OOO;
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

#ifndef MYPYC_DECLARED_tuple_T4OOOO
#define MYPYC_DECLARED_tuple_T4OOOO
typedef struct tuple_T4OOOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
    PyObject *f3;
} tuple_T4OOOO;
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
    PyObject *__value;
    PyObject *__times;
    CPyTagged __index;
} faster_eth_utils___abi____repeatObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t mypyc_running;
    PyObject *___mypyc_generator_frame_attribute__formatter;
    CPyTagged ___mypyc_generator_frame_attribute__at_index;
    PyObject *___mypyc_generator_frame_attribute__value;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_frame_attribute__item;
    PyObject *___mypyc_temp__3_faster_eth_utils___applicators___apply_formatter_at_index_gen_1;
    PyObject *___mypyc_temp__3_faster_eth_utils___applicators___apply_formatter_at_index_gen_2;
} faster_eth_utils___applicators___apply_formatter_at_index_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t mypyc_running;
    PyObject *___mypyc_generator_frame_attribute__formatters;
    PyObject *___mypyc_generator_frame_attribute__sequence;
    int32_t ___mypyc_next_label__;
    int64_t ___mypyc_temp__3_faster_eth_utils___applicators___apply_formatters_to_sequence_gen_0;
    PyObject *___mypyc_temp__2_faster_eth_utils___applicators___apply_formatters_to_sequence_gen_0;
    PyObject *___mypyc_temp__2_faster_eth_utils___applicators___apply_formatters_to_sequence_gen_1;
} faster_eth_utils___applicators___apply_formatters_to_sequence_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_formatters;
    PyObject *_get_value;
} faster_eth_utils___applicators___apply_formatters_to_dict_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___applicators___get_value_apply_formatters_to_dict_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t mypyc_running;
    PyObject *___mypyc_generator_frame_attribute__formatter;
    PyObject *___mypyc_generator_frame_attribute__value;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__2_faster_eth_utils___applicators___apply_formatter_to_array_gen_0;
} faster_eth_utils___applicators___apply_formatter_to_array_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_key_mappings;
    PyObject *_get_key;
} faster_eth_utils___applicators___apply_key_map_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_eth_utils___applicators___get_key_apply_key_map_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
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
    PyObject *_bound_arg;
    PyObject *_method;
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
    uint32_t mypyc_running;
    PyObject *___mypyc_generator_frame_attribute__units_iter;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__3_faster_eth_utils___humanize____consume_leading_zero_units_gen_0;
} faster_eth_utils___humanize____consume_leading_zero_units_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t mypyc_running;
    CPyTagged ___mypyc_generator_frame_attribute__seconds;
    int32_t ___mypyc_next_label__;
    CPyTagged ___mypyc_generator_frame_attribute__remainder;
    CPyTagged ___mypyc_generator_frame_attribute__duration;
    PyObject *___mypyc_temp__2_faster_eth_utils___humanize____humanize_seconds_gen_0;
} faster_eth_utils___humanize____humanize_seconds_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t mypyc_running;
    PyObject *___mypyc_generator_frame_attribute__values;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__2_faster_eth_utils___humanize____find_breakpoints_gen_0;
} faster_eth_utils___humanize____find_breakpoints_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t mypyc_running;
    PyObject *___mypyc_generator_frame_attribute__values;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__2_faster_eth_utils___humanize____extract_integer_ranges_gen_0;
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

#endif
