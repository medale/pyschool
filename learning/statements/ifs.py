# https://docs.python.org/3/reference/compound_stmts.html#the-if-statement

def ifs():
    count = 15

    # first condition evaluating to true gets executed
    if count > 10:
        print('big')
    elif count < 10 and count > 5:
        print('medium')
    else:
        print('small')


def nested_ifs(count):
    # Can have nested ifs
    if count % 2 == 0:
        print('even number')
    else:
        print('odd number')
        if count % 3 == 0:
            # new block of code
            print('multiple of 3')
            if count % 5 == 0:
                # new block of code
                print('multiple of 5')
