import string
import unittest
import learning.solutions.soln_types_exercises as tex

class TestTypes(unittest.TestCase):
    """ run via python -m unittest discover
    """
    def test_letter_frequency_simple(self):
        simple = '$abc_ ABC!'

        # simple should result in a:2,b:2,c:2,d:1...z:1
        list_of_counts = ([2] * 3) + ([0] * 23)
        letter_count_tuples = zip(string.ascii_lowercase, list_of_counts)
        expected = dict(letter_count_tuples)

        self.assertEqual(tex.letter_frequency(simple), expected)


    def test_empty_string(self):
        para = ''
        list_of_counts = ([0] * 26)
        letter_count_tuples = zip(string.ascii_lowercase, list_of_counts)
        expected = dict(letter_count_tuples)

        self.assertEqual(tex.letter_frequency(para), expected)


if __name__ == '__main__':
    unittest.main()