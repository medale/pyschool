import string

def letter_frequency(paragraph):
    """Count frequency of letters in argument string.

    Count the frequency of letters occurring in the argument string.
    Ignore capitalization (i.e. Anna - a: 2, n: 2). Ignore all whitespace,
    non-alpha characters.

    Args:
        paragraph (str): The paragraph to analyze

    Returns:
        a dict containing all lowercase letters of the alphabet and their
        occurrence count in the given paragraph. Letters that did not appear
        should have an occurrence count of 0.
    """
    all_lower = paragraph.lower()

    # filter out non-letters
    all_alphas = [c for c in all_lower if c.isalpha()]

    # create empty alpha dict with all 26 letters of count 0
    twenty_six_zeros = [0] * 26
    letter_count_tuples = zip(string.ascii_lowercase, twenty_six_zeros)
    alpha_dict = dict(letter_count_tuples)

    for c in all_alphas:
        alpha_dict[c] += 1

    return alpha_dict
