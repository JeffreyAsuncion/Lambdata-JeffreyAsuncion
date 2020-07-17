import unittest
import pandas as pd
from my_lambdata.ds_utilities import enlarge, MyDataSplitter
from my_lambdata.ds_utilities import states_abbr_to_full
from my_lambdata.ds_utilities import states_full_to_abbr


class TestDsUtilitiesEnlarge(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(3), 3000)

    def test_states_abbr_to_full(self):
        self.assertEqual(states_abbr_to_full("NY"), "New York")

    def test_states_full_to_abbr(self):
        self.assertEqual(states_full_to_abbr("New York"), "NY")

    def test_date_divider(self):
        # Create MyDataSplitter object
        splitter = MyDataSplitter()
        raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
                    'age': [20, 19, 22, 21],
                    'favorite_color': ['blue', 'red', 'yellow', "green"],
                    'grade': [88, 92, 95, 70],
                    'birth_date': ['01-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
        splitter.df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
        date_col = 'birth_date'

        current_shape = splitter.df.shape[1]
        expected_shape = current_shape + 3

        converted_df = splitter.date_divider(date_col)

        self.assertEqual(expected_shape, converted_df.shape[1])




if __name__ == '__main__':
    unittest.main()

