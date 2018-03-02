# https://docs.python.org/3/library/stdtypes.html#lists
def lists():
    py_invent = ['Guido', 'van', 'Rossum']

    # List as sequence/iteration, index, slices... - new list
    py_invent[0]      # 'Guido'
    py_invent[:-1]    # ['Guido', 'van']

    # size/count number of elements in list
    len(py_invent)

    numpy_invent = ['Travis', 'Oliphant']

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


