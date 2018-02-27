import sys


# *args is used to send a non-keyworded variable length argument list to the function.
# https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
def main(*args):
    # indents indicate nesting
    print(type(args))
    strings()
    lists()
    dicts()


def strings():
    # usually use single quotes but can use double quotes
    # assign our first variable - s1
    s1 = 'hello, I am a String and a sequence'
    my_type = type(s1)

    # String formatting/substitution - https://pyformat.info/
    # old style: print('s1 is of type %s' % myType)
    # new style:
    print('s1 is of type {}'.format(my_type))

    # concat and repetition
    foo = 'f' + 'oo'
    foobar = foo + 'bar'
    whole_lotta_foos = foo * 8

    # Immutability - 'str' object does not support item assignment
    # foo[0] = 'b'   # throws TypeError

    strings_as_sequences(s1)

    more_methods_on_strings()


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


def dicts():

    # No order!
    ping_pong_scores = {'Chang': 98, 'Steve': 82, 'Amit': 1}
    ping_pong_scores['Chang']
    ping_pong_scores['Chang'] += 1

    # Add an element
    ping_pong_scores['Troy'] = 70

    # m_score = ping_pong_scores['Markus'] # KeyError: 'Markus'
    m_score = ping_pong_scores.get('Markus',0)

    # dict as an informal way of creating records
    record_1 = {'first': 'Foo', 'last': 'Bar', 'age': 42}
    record_1['age']

    # list - otherwise dict_keys, dict_values
    names = list(ping_pong_scores.keys())
    scores = list(ping_pong_scores.values())

    # sort by key
    sorted(ping_pong_scores)

    # sorts values - lowest to highest
    sorted(ping_pong_scores.items(), key=lambda kv: kv[1])

    # sorts values - highest to lowest
    sorted(ping_pong_scores.items(), key=lambda kv: kv[1], reverse=True)


def strings_as_sequences(s1):
    # Things to do to sequences
    s1_len = len(s1)
    print('Length of s1 is {:d}'.format(s1_len))

    first_letter = s1[0]

    # negative indices - start from end with -1
    last_letter = s1[-1]

    # slice and dice - inclusive:exclusive
    string_slice = s1[14:20] #The word 'String'

    # slice - left bound default is 0, right bound length of string
    no_first_letter = s1[1:]  # everything but first letter 1:len(s1)
    up_to_string = s1[:20] # 0 (inclusive) to 20 (exclusive): 'hello, I am a String'
    no_last_letter = s1[:-1] # everything but last letter 0:-1

    # throws IndexError: string index out of range
    # s1[-100]


def more_methods_on_strings():
    s2 = "Now,IS,the,Time,The,TIME,is,now,OR,NeVer"
    first_comma_index = s2.index(",")
    last_comma_index = s2.rindex(",")

    words = s2.split(",")

    # also upper() - with for comprehension (later)
    lower_words = [w.lower() for w in words]

    s3 = """I can't spel.
    They can't spel either."""

    correct_s3 = s3.replace("spel","spell")

    # find index of first can't or -1
    cant_index = s3.find("can't")

    not_found = s3.find('foo')

    # show all methods for str objects or dir(str)
    dir(s3)

    # show docs for a specific method
    help(s3.center)


if __name__ == '__main__':
    print('%s is being run by itself. Calling main' % __file__)
    main(sys.argv)
else:
    print('%s is being imported from another module' % __file__)