# https://docs.python.org/3/library/stdtypes.html#tuples
import string

def tuples():
    # Immutable
    tup = ('foo', 100, 42)

    'foo' in tup # true

    word = tup[0]
    word_count = tup[1]
    doc_count = tup[2]

    w, w_count, d_count = tup

    empty_tup = ()

    # create tuples from two lists via zip
    lower_upper_tuples = zip(string.ascii_lowercase, string.ascii_uppercase)

    # use two tuples to create a dict
    lower_upper_dict = dict(lower_upper_tuples)
