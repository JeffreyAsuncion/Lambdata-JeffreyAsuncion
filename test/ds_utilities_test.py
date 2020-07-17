import unittest
import pandas as pd
from my_lambdata.ds_utilities import enlarge
from my_lambdata.ds_utilities import test_data_divider

class TestDsUtilitiesEnlarge(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(3), 300)

    def test_data_divider(self):
        raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
                    'age': [20, 19, 22, 21],
                    'favorite_color': ['blue', 'red', 'yellow', "green"],
                    'grade': [88, 92, 95, 70],
                    'birth_date': ['01-02-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
        df3 = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
        date_col = 'birth_date'

        current_shape = df.shape[1]
        expected_shape = current_shape + 3

        # Create MyDataSplitter Object
        splitter = MyDataSplitter(df, features=['age','favorite_color','birth_date'], target='grade'
        converted_df = date_divider(df, date_col)

        self.assertEqual(expected_shape, converted_df.shape[1])

if __name__ == '__main__':
    unittest.main()

