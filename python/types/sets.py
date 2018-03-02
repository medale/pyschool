def sets():

    set1 = {'a','b','c'}

    set2 = {'d', 'e', 'c'}

    # union of sets as a new set
    set_union = set1.union(set2)

    set3 = {'m','d'}

    # mutable sets - add all unique elements from set2
    set3.update(set2)

    list1 = [2,1,1,4,5,1,6,6,4]

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