import string
import unittest
import python.exercises.types_exercises as tex

class TestTypes(unittest.TestCase):
    """ run via python -m unittest discover
    """
    def test_letter_frequency_simple(self):
        simple = string.ascii_lowercase + string.ascii_uppercase
        twenty_six_two_strs = '2' * 26
        list_of_two_ints = [int(c) for c in twenty_six_two_strs]
        letter_count_tuples = zip(string.ascii_lowercase, list_of_two_ints)
        expected = dict(letter_count_tuples)
        self.assertEqual(tex.letter_frequency(), expected)

if __name__ == '__main__':
    unittest.main()