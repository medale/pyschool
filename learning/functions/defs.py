def no_return_is_none():
    print("no return")
    # returning None


def args_by_position(start,finish):
    sum_range = range(start,finish)

    # return statement determines return type
    return sum(sum_range)


def bad_func():
    # I don't get executed until runtime
    return funky


def intersect(xs, ys):
    common = []
    for x in xs:
        if x in ys:
            common.append(x)
    return common


def complex_processing(a):
    # local function - only call from within complex_processing
    # has access to outer function arguments
    def helper():
        if a > 10:
            # function can have multiple returns
            return 'foo'
        elif a < 0:
            return 'bar'

    # local variable
    complex_result = helper()
    return complex_result


def main():
    none_result = no_return_is_none()
    sum_to_100 = args_by_position(1, 101)

    # type of bad is function - still not executed
    bad = bad_func
    bad_func()  # function gets actually executed - error!

    # dynamic typing polymorphism - first and second arg must support 'in'
    common_letters = intersect('monty', 'python')
    common_elements = intersect([1, 2, 3], [3, 4, 1])
    common_keys = intersect(['a', 'c'], {'a': 1, 'b': 0})

    res0 = complex_processing(-10)
    res1 = complex_processing(12)
    res2 = complex_processing(7)


if __name__== "__main__":
    main()
