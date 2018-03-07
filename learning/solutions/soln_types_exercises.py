import string

def three_list_to_record(three_list):
    """Helper function for csv_to_records to convert list with three
    [lname,fname,age_str] to {'last_name': lname, 'first_name': fname, 'age': age_int}
    Code checks argument for three entries and third entry being convertible to int.

    Args:
        three_list(list(str,str,int)): [lname,fname,age]

    Returns:
        {'last_name': lname, 'first_name': fname, 'age': age_int}

    Raises:
        ValueError: three_list has not three entries or entry 3 is not int.
    """
    if len(three_list) != 3:
        raise ValueError('three_list argument did not have three entries')

    lname, fname, age_str = three_list

    if age_str.isdigit():
        age_int = int(age_str)
    else:
        raise ValueError('three_list[2] (age_str) should convertible to int')

    return {'last_name': lname, 'first_name': fname, 'age': age_int}


def csv_to_records(csv_lines):
    """Convert lines with comma-separated values into a list of
    dict objects.

    Each line has three fields:
    last_name, first_name, age

    So the csv_lines:
    doe,john,42
    smith,jane,34

    should create: [{'last_name': 'doe', 'first_name': 'john', 'age': 42},
    {'last_name': 'smith', 'first_name': 'jane', 'age': 34}]

    Note: a valid age should be an int value (don't worry about range).

    Save lines that have too few, too many or improper fields in a
    bad_lines list and return as second entry of two tuple.

    Args:
        csv_lines (str): The csv lines to convert to dicts. Could be
        an empty string (return empty list). Lines are separated by newline
        character (\n).

    Returns:
        A two-tuple with a (list of dicts of good lines, list of bad lines)
    """
    bad_lines = []
    records = []

    lines = csv_lines.split('\n')

    for line in lines:
        fields = line.split(',')
        if len(fields) == 3:
            lname, fname, age_str = fields
            try:
                record = three_list_to_record([lname,fname,age_str])
                records.append(record)
            except ValueError:
                bad_lines.append(line)
            else:
                bad_lines.append(line)
        else:
            bad_lines.append(line)

    return (records, bad_lines)


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
