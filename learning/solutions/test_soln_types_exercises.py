import string
import unittest
import learning.solutions.soln_types_exercises as tex

class TestTypes(unittest.TestCase):
    """ run via python -m unittest discover
    """
    def test_three_list_to_record_sunny_day(self):
        input = ['miller' ,'glenn' ,'36']
        result = tex.three_list_to_record(input)

        self.assertEqual(result, {'last_name': 'miller',
                                  'first_name': 'glenn',
                                  'age': 36})


    def test_three_list_short(self):
        input = ['short','entry']
        with self.assertRaises(ValueError):
            tex.three_list_to_record(input)


    def test_three_list_long(self):
        input = ['long', 'entry', '45', 'extra']
        with self.assertRaises(ValueError):
            tex.three_list_to_record(input)


    def test_three_list_no_int(self):
        input = ['miller' ,'glenn' ,'XL']
        with self.assertRaises(ValueError):
            tex.three_list_to_record(input)


    def test_csv_to_records_mixed(self):
        csv_lines_str = """miller,glenn,36
bad,age,fifteen
fitzgerald,ella,28
short,entry
armstrong,louis,45
long,entry,45,extra"""

        records, bad_lines = tex.csv_to_records(csv_lines_str)

        lines = ['miller,glenn,36', 'fitzgerald,ella,28', 'armstrong,louis,45']
        expected_records = []
        for line in lines:
            threes = line.split(',')
            record = tex.three_list_to_record(threes)
            expected_records.append(record)

        expected_bad_lines = ['bad,age,fifteen','short,entry','long,entry,45,extra']
        self.assertEqual(records, expected_records)
        self.assertEqual(bad_lines, expected_bad_lines)


    def test_csv_to_records_empty(self):
        records, bad_lines = tex.csv_to_records('')
        self.assertTrue(len(records) == 0)
        self.assertTrue(bad_lines == [''])


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