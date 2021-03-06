import copy

# https://docs.python.org/3/library/stdtypes.html#lists
def lists():
    # empty list
    empty_list = []

    # list from an iterable
    letters = list('these are the letters')

    # Create new list with [] construct
    py_invent = ['Guido', 'van', 'Rossum']

    # Create new list using iterator over argument
    my_letters = list('abcd')

    # List as sequence/iteration, index, slices... - new list
    py_invent[0]      # 'Guido'
    py_invent[:-1]    # ['Guido', 'van']

    # size/count number of elements in list
    len(py_invent)

    numpy_invent = ['Travis', 'Oliphant']

    # unpacking a list - exact match
    fname, lname = numpy_invent

    # unpack a list - first element, list of remaining elements
    head, *tail = py_invent

    # concat, multiply - new lists
    inventors = py_invent + numpy_invent

    # add numpy_event to content of all_inventors
    all_inventors = py_invent
    all_inventors.extend(numpy_invent)

    items = ['bread', 'butter']
    items.insert(0, 'beer')
    items.append('eggs')
    items.remove('butter')
    my_beer = items.pop(0)

    # remove all elements
    items.clear()

    letters = ['a', 'c', 'd', 'c']
    letters.sort()

    # named parameter (also key function to apply to each element)
    letters.sort(reverse=True)

    # count occurrences of objects in list
    letters.count('c')

    # create a list with 10 zeros
    ten_zeros = [0] * 10

    # List for comprehension
    cap_letters = [l.capitalize() for l in letters]

    # range: inclusive, exclusive, step
    one_to_19 = list(range(1, 20))

    # List comprehension with conditional
    evens = [n for n in one_to_19 if n % 2 == 0]

    # old - potentially slower
    old_evens = []
    for n in one_to_19:
        if n % 2 == 0:
            old_evens.append(n)

    # however, if we want a multi-bucket sort in one pass
    evens_bucket = []
    odds_bucket = []
    for n in one_to_19:
        if n % 2 == 0:
            evens_bucket.append(n)
        else:
            odds_bucket.append(n)

    # two names pointing to same list object
    original_list = ['a', 'b', 'c']

    # make an immutable string from list - elements separated by ,
    comma_sep_orig1 = ','.join(original_list)

    additional_name = original_list

    additional_name.append('d')

    comma_sep_orig = ','.join(original_list)
    comma_sep_add = ','.join(additional_name)

    # make a shallow copy
    shallow_copy = original_list[:]
    shallow_copy2 = original_list.copy()

    original_list.append('e')

    # if list points to mutable objects - module copy - deep copy
    deep_list = [['a','b'], ['c','d']]
    shallow_deep_list = deep_list[:]

    shallow_deep_list[0][0] = 'f'

    deep_deep_copy = copy.deepcopy(deep_list)
