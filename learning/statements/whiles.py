#

def whiles():

    numbers = range(10)
    # unpacking - ends when tail == []
    head, *tail = numbers
    done = False
    while not done:
        head, *tail = tail
        print(head)
        done = len(tail) == 0

