import sys


# *args is used to send a non-keyworded variable length argument list to the function.
# https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
def main(*args):
    # indents indicate nesting
    print(type(args))


if __name__ == '__main__':
    print('%s is being run by itself. Calling main' % __file__)
    main(sys.argv)
else:
    print('%s is being imported from another module' % __file__)