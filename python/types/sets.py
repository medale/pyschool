# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
def sets():

    set1 = {'a', 'b', 'c'}

    set2 = {'d', 'e', 'c'}

    # union of sets as a new set; also | operator
    set_union = set1.union(set2)

    set3 = {'m', 'd'}

    # mutable sets - add all unique elements from set2
    set3.update(set2)

    # remove element 'm' from set3
    set3.discard('m')

    # common elements in both sets; also & operator: {'c'}
    common_elements = set1.intersection(set2)

    # in set1 but not set2; also - operator: {'a', 'b'}
    set1_but_not_set2 = set1.difference(set2)

    list1 = [2, 1, 1, 4, 5, 1, 6, 6, 4]

    # unique elements only - sets are unordered, no indices
    uniques_for_list1 = set(list1)

    # a little control structure if,elif,else:
    if 7 in uniques_for_list1:
        print('Yeah 7')
    elif 9 in uniques_for_list1:
        print('Yeah 9')
    elif 1 in uniques_for_list1:
        print('Yeah 1')
    else:
        print("no 1, 7 or 9")

    # compare two sets: isdisjoint, issubset, issuperset also <=, <, >=, >
    # False - they have 'c' in common
    disjoint = set1.isdisjoint(set2)
