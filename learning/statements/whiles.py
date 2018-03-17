# https://docs.python.org/3/reference/compound_stmts.html#while

def whiles():

    numbers = range(10)
    # unpacking - ends when tail == []
    head, *tail = numbers
    done = False

    # break exists the loop
    # continue goes back to checking the loop condition
    while not done:
        head, *tail = tail
        print(head)
        done = len(tail) == 0

