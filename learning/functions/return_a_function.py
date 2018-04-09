import os
import os.path as path


def filter_by_extension(ext):
    """
    A higher-order function that returns a function
    that given a filename filters by the extension
    argument.
    :param ext: the return function will return true if a filename ends with ext
    :return: a one-arg function that takes a filename and returns true if filename ends with ext
    """
    def filt(filename):
        return filename.endswith(ext)
    return filt


def filter_not_by_starting_symbol(symbols):
    """
    A higher-order function that returns a function that filters
    filenames to filenames NOT starting with symbols
    :param symbols:
    :return:
    """
    def filt(filename):
        return not any([filename.startswith(s) for s in symbols])
    return filt


def filter_by_contains(fragment):
    """
    A higher-order function that returns a function that checks whether
    a filename contains fragment.
    :param fragment:
    :return:
    """
    def filt(filename):
        return fragment in filename
    return filt


def list(directory=os.getcwd(), filter_funcs=[]):
    """
    List files in directory and return files that test true for all
    filter_funcs.

    :param directory:
    :param filter_funcs:
    :return:
    """
    # arguments with default values
    files_and_dirs = os.listdir(directory)
    files = [f for f in files_and_dirs if path.isfile(path.join(directory, f))]
    good_files = []
    for f in files:
        filter_results = [filt(f) for filt in filter_funcs]
        if all(filter_results):
            good_files.append(f)
    return good_files


def main():
    # we want files that end with .py
    # don't start with _ or .
    # contain an 'i'
    end_py_func = filter_by_extension('.py')
    not_hidden_func = filter_not_by_starting_symbol(['_', '.'])
    has_i = filter_by_contains('i')

    cwd = os.getcwd()
    # on console we run from pyschool directory
    base_dir = 'learning/statements'
    if cwd.endswith('functions'):
        # in debug mode we run from functions directory
        base_dir = '../../learning/statements'

    files_of_interest = list(base_dir, [end_py_func, not_hidden_func, has_i])
    print('\n'.join(files_of_interest))

    # use both default arguments
    files_in_current_dir = list()

    py_in_current_dir = list(filter_funcs=[filter_by_extension('.py')])


if __name__== "__main__":
    main()
