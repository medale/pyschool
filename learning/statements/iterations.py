import os
import random
import string

def iterations():

    my_list = ['a','b','c']

    # also sets, dictionary (keys), dict.items (k,v)...
    for c in my_list:
        print(c)

    # if using relative file paths - where does this get executed from?
    # from statements if using Debugger
    # from pyschool if using Python Console...
    print(os.getcwd())

    # file iterator - gets iter (calling __iter__)
    # calls __next__, raises StopIteration
    for line in open('three_lines.txt'):
        # each line has \n - end '' removes
        print(line, end='')

    # behind the scenes - calls to __iter__/__next__ until StopIteration
    f = open('three_lines.txt')
    # a file object is an iterator so we don't need
    # iter = f.__iter__()
    done = False
    while not done:
        try:
            line = f.__next__()
            if not line:
                done = True
            print(line, end='')
        except StopIteration:
            print("\nIt's the end, my friend")
            break

    # stepping through a dictionary
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key, d[key])

    # stepping through iterables - like enumerate
    l = ['a', 'b', 'c']
    # create (0, 'a') etc. tuples
    e = enumerate(l)
    iter = iter(e)
    element1 = next(iter)


def comprehensions():
    l = range(100)
    # new_list = [str(elem) for elem in old_list if test]
    # 1. call next on iterator over old_list to get new elem
    # 2. check if elem passes the filter's test
    # 3. If pass - return elem as part of the new list
    # 4. If fail - goto 1
    new_l = [num for num in l if num % 2 == 0]

    letters = ['A', 'c', 'C', 'D', 'D', 'e']
    unique_uppers = {letter for letter in letters if letter.isupper()}

    lowers = [letter for letter in string.ascii_lowercase]

    # ord(c) returns ascii value for c
    # chr(num) converts num to character
    ascii_vals = [ord(letter) for letter in lowers]

    ascii_dict = {letter: ascii for letter,ascii in zip(lowers, ascii_vals)}


def functions_on_iterables():
    # list, set, dict (iterable over two-tuples), enumerate
    dupes = 'aabbccdd'
    ldupes = list(dupes)
    sdupes = set(dupes)
    ddupes = dict(enumerate(dupes))

    # zip returns iterator - convert to list
    pairs = list(zip('abcd','ghi'))

    # apply method upper of str objects for each letter in dupes
    uppers = list(map(str.upper, dupes))

    order = sorted(sdupes)

    joined = ','.join(dupes)

    # sum, any, all, max, min
    sum(range(101)) #(n * (n+1)/2)

    results = [True, False, True]
    any_trues = any(results)
    all_trues = all(results)

    random_nums = [random.randint(0,100) for x in range(101)]
    high = max(random_nums)
    low = min(random_nums)

    low_random_nums = list(filter(my_filter, random_nums))

    # or lambda function
    low_random_nums_lambda = list(filter(lambda n: n < 50, random_nums))


def my_filter(n):
    return n < 50


if __name__== "__main__":
    iterations()
    comprehensions()