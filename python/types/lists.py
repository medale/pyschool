def lists():
    py_invent = ['Guido','van','Rossum']

    # List as sequence/iteration, index, slices... - new list
    py_invent[0]      # 'Guido'
    py_invent[:-1]    # ['Guido', 'van']

    len(py_invent)

    numpy_invent = ['Travis', 'Oliphant']

    # concat, multiply - new lists
    inventors = py_invent + numpy_invent

    # add numpy_event to content of all_inventors
    all_inventors = py_invent
    all_inventors.extend(numpy_invent)

    items = ['bread','butter']
    items.insert(0,'beer')
    items.append('eggs')
    items.remove('butter')
    my_beer = items.pop(0)

    letters = ['a','c','d','c']
    letters.sort()

    # named parameter (also key function to apply to each element)
    letters.sort(reverse=True)