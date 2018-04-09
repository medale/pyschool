from functools import reduce


def lambada():
    """
    Functional programming with map and lambda.
    :return: None
    """
    words = ['this', 'is', 'a', 'test', 'of', 'the']
    lengths = map(lambda w: len(w), words)
    print(",".join(map(lambda n: str(n), lengths)))


def sorted_lambda():
    """
    lambda key function on sorted method.
    :return: None
    """
    nums = [('apple', 1), ('orange', 3), ('tea', 4), ('beer', 2),
            ('wine', 7), ('gummibears', 3), ('bread', 6)]
    most_frequents = sorted(nums, key=lambda tup: tup[1], reverse=True)


def combine_by_function(iterable, start_val, combine_func):
    """
    An approximation of the reduce method.
    :param iterable: input list etc.
    :param start_val: a starting value
    :param combine_func: a function taking two arguments and returning a value.
    :return: combined value
    """
    count = len(iterable)
    if count == 0:
        return start_val
    else:
        last_val = start_val
        index = 0
        while index < count:
            curr_elem = iterable[index]
            last_val = combine_func(last_val, curr_elem)
            index += 1
        return last_val


def main():
    lambada()
    sorted_lambda()

    nums = [2, 3, 4]
    sum_of_nums = combine_by_function(nums, 0, lambda x, y: x + y)
    sum_of_squares = combine_by_function(nums, 0, lambda x, y: x + y * y)
    multiplied = combine_by_function(nums, 1, lambda x, y: x * y)
    squares = combine_by_function(nums, [], lambda l, y: l + [y*y])

    sums = reduce(lambda x, y: x + y, nums)
    m2 = reduce(lambda x, y: x * y, nums, 10)
    squares = reduce(lambda l, y: l + [y * y], nums, [])


if __name__== "__main__":
    main()