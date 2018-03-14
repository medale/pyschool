# https://docs.python.org/3/reference/compound_stmts.html#the-if-statement

def ifs():
    count = 15

    if count > 10:
        print('big')
    elif count < 10 and count > 5:
        print('medium')
    else:
        print('small')