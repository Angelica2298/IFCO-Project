import os
import sys
import unittest
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.Exercise2 import get_full_name

class TestOrdersDataFrame(unittest.TestCase):
    def setUp(self):
        self.df_1 = pd.DataFrame({
            'contact_data': [
                '[{"contact_name":"Curtis", "contact_surname":"Jackson", "city":"Chicago", "cp": "12345"}]',
                '{"contact_name":"Maria", "contact_surname":"Theresa", "city":"New York", "cp": "54321"}',
                '[{"city":"Los Angeles", "cp": "98765"}]'
            ]
        })

    def test_full_names_ok(self):
        full_names = ['Curtis Jackson', 'Maria Theresa', 'John Doe']
        self.df_1['contact_full_name'] = self.df_1['contact_data'].apply(get_full_name)
        self.assertListEqual(self.df_1['contact_full_name'].tolist(), full_names)

if __name__ == '__main__':
    unittest.main()