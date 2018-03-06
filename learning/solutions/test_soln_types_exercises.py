import string
import unittest
import learning.solutions.soln_types_exercises as tex

class TestTypes(unittest.TestCase):
    """ run via python -m unittest discover
    """
    def test_three_list_to_record(self):
        inputs = [['miller' ,'glenn' ,36],
                  ['short','entry'],
                  ['long', 'entry', 45, 'extra']]



    def test_csv_to_records_mixed(self):
        csv_lines = """miller,glenn,36
        bad,age,fifteen
        fitzgerald,ella,28
        short,entry
        armstrong,louis,45
        long,entry,45,extra
        """

        expected = {}


    def test_csv_to_records_empty(self):
        pass

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