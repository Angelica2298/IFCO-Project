import os
import sys
import unittest
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.Exercise3 import get_full_address

# Unit Test Exercise 3: DataFrame of Orders with Contact Address #
##################################################################

class TestOrdersDataFrame(unittest.TestCase):
    def setUp(self):
        # Data for our tests
        self.df_1 = pd.DataFrame({
            'contact_data': [
                '[{"contact_name":"Curtis", "contact_surname":"Jackson", "city":"Chicago", "cp": "12345"}]',
                '{"contact_name":"Maria", "contact_surname":"Theresa", "city":"New York", "cp": "54321"}',
                '[{"city":"Los Angeles"}]'
            ]
        })

    def test_full_address_ok(self):
        address = ['Chicago, 12345', 'New York, 54321', 'Los Angeles, UNK00']
        self.df_1['contact_address'] = self.df_1['contact_data'].apply(get_full_address)
        self.assertListEqual(self.df_1['contact_address'].tolist(), address)

if __name__ == '__main__':
    unittest.main()