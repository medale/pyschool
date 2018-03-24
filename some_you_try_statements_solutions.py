# Write a for loop that counts how many lines there are in docs/samples/ApacheFoundation.html

def how_many_lines():
    line_count = 0
    for line in open('docs/samples/ApacheFoundation.html'):
        line_count += 1
    return line_count

def python_in_html():
    for line in open('docs/samples/ApacheFoundation.html'):
        if 'Python' in line:
            print(line)


def main():
    line_count = how_many_lines()
    print('there were %d lines' % line_count)


if __name__== "__main__":
    main()