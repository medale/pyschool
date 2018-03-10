def three_list_to_record(three_list):
    """Helper function for csv_to_records to convert list with three
    entries [lname,fname,age_str] to {'last_name': lname, 'first_name': fname, 'age': age_int}
    Code checks argument for three entries and third entry being convertible to int.

    Args:
        three_list(list(str,str,str)): [lname,fname,age]

    Returns:
        {'last_name': lname, 'first_name': fname, 'age': age}

    Raises:
        ValueError: three_list has not three entries or entry 3 is not int.
    """
    if len(three_list) != 3:
        raise ValueError('three_list argument did not have three entries')

    if not isinstance(three_list[2], int):
        raise ValueError('three_list[2] (age) should be an int')

    pass


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

    Note: age should be an int value.

    Save lines that have too few or too many fields in a bad_lines list
    and return as second entry of two tuple.

    Args:
        csv_lines (str): The csv lines to convert to dicts. Could be
        an empty string (return empty records list and bad_lines of ['']).

    Returns:
        A two-tuple with a (list of dicts of good lines, list of bad lines)
    """

    """
    use:    try:
                record = three_list_to_record([lname,fname,age_str])
                records.append(record)
            except ValueError:
                bad_lines.append(line)
    """
    pass


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
    pass