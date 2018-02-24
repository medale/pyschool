import sys

# *args is used to send a non-keyworded variable length argument list to the function.
# https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
def main(*args):
    # indents indicate nesting
    print(type(args))
    strings()

def strings():
    # usually use single quotes but can use double quotes
    # assign our first variable - s1
    s1 = 'hello, I am a String and a sequence'
    myType = type(s1)

    # String formatting/substitution - https://pyformat.info/
    # old style: print('s1 is of type %s' % myType)
    # new style:
    print('s1 is of type {}'.format(myType))

    # Things to do to sequences
    s1Len = len(s1)
    print('Length of s1 is {:d}'.format(s1Len))

    firstLetter = s1[0]
    print('First letter in s1 is {}'.format(firstLetter))

    # negative indices - start from end with -1
    lastLetter = s1[-1]
    print('Last letter in s1 is {}'.format(lastLetter))

    # slice and dice - inclusive:exclusive
    stringSlice = s1[14:20] #The word 'String'

    # slice - left bound default is 0, right bound length of string
    s1[1:]  # everything but first letter 1:len(s1)
    s1[:20] # 0 (inclusive) to 20 (exclusive): 'hello, I am a String'
    s1[:-1] # everything but last letter 0:-1

    # concat and repetition
    foo = 'f' + 'oo'
    foobar = foo + 'bar'
    wholeLottaFoos = foo * 8

    # Immutability - 'str' object does not support item assignment
    foo[0] = 'b'

    # IndexError: string index out of range
    s1[-100]

if __name__ == '__main__':
    print('%s is being run by itself. Calling main' % __file__)
    main(sys.argv)
else:
    print('%s is being imported from another module' % __file__)