# https://docs.python.org/3/library/stdtypes.html#tuples
def tuples():
    # Immutable
    tup = ('foo', 100, 42)

    'foo' in tup # true

    word = tup[0]
    word_count = tup[1]
    doc_count = tup[2]

    w, w_count, d_count = tup

    empty_tup = ()
