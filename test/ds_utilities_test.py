import unittest
import pandas as pd
from my_lambdata.ds_utilities import enlarge
from my_lambdata.ds_utilities import states_abbr_to_full
from my_lambdata.ds_utilities import states_full_to_abbr
# from my_lambdata.ds_utilities import test_data_divider

class TestDsUtilitiesEnlarge(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(3), 3000)

    def test_states_abbr_to_full(self):
        self.assertEqual(states_abbr_to_full("NY"), "New York")

    def test_states_full_to_abbr(self):
        self.assertEqual(states_full_to_abbr("New York"), "NY")


if __name__ == '__main__':
    unittest.main()

