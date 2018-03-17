import os

def iterations():

    my_list = ['a','b','c']

    # also sets, dictionary (keys), dict.items (k,v)...
    for c in my_list:
        print(c)

    # if using relative file paths - where does this get executed from?
    # from statements if using Debugger
    # from pyschool if using Python Console...
    print(os.getcwd())

    # file iterator - gets iter (calling __iter__)
    # calls __next__, raises StopIteration
    for line in open('three_lines.txt'):
        # each line has \n - end '' removes
        print(line, end='')


    f = open('three_lines.txt')
    iter = f.__iter__()
    done = False
    while not done:
        try:
            line = iter.__next__()
            if not line:
                done = True
            print(line, end='')
        except StopIteration:
            print("It's the end, my friend")
            break


if __name__== "__main__":
    iterations()