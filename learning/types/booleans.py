# https://docs.python.org/3/library/stdtypes.html#boolean-values
def booleans():

    # two constant objects: True or False
    true_val = 'a' == 'a'

    false_val = 'a' == 'b'

    # Boolean operations: and, or, not
    not_true = not True

    # short circuit eval or - first part is true, don't need to eval second for or
    # short circuit eval and - first part is false, don't need to eval second half

    # No IndexError thanks to short-circuit evaluation
    short_list = [1,2]
    short_circuit_eval_or = (10 != 1) or short_list[99]

    # short_list[99]

    # Truth value testing - https://docs.python.org/3/library/stdtypes.html#truth
    # Not just booleans in if statements...

    # False - zero of any numeric type
    zero_evaluates_to_false = bool(0)
    non_zero_evaluates_to_true = bool(1000)

    none_evaluates_to_false = bool(None)

    # empty sequences or collections are False
    empty_string_evaluates_to_false = bool('')

    empty_dict_evaluates_to_false = bool({})

    # comparison operators return boolean: ==, !=, <, >, <=, >=
    my_comparison = 10 > 8