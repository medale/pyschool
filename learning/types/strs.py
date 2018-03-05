# Built-in type str - not 'string' class
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
import string

def strs():
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

    strs_as_sequences()

    more_methods_on_strs()

    checking_str_values()


def strs_as_sequences():
    s1 = 'hello, I am a String and a sequence'
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


def more_methods_on_strs():
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


def checking_str_values():

    # True
    is_alpha = 'abcDEF'.isalpha()

    # True
    is_alpha_numeric = 'aZ12'.isalnum()

    # False
    is_all_digits = 'Working 9 to 5'.isdigit()

    # all lower case ascii
    lowers = string.ascii_lowercase

    # all upper case ascii
    uppers = string.ascii_uppercase

    # all lower and upper case ascii
    letters = string.ascii_letters