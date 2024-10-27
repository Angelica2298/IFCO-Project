import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.Exercise1 import crate_distribution

class TestCrateDistribution(unittest.TestCase):
    def setUp(self):
        # Data for our tests
        data = {
            'company_name': ['Company A', 'Company A', 'Company B', 'Company A', 'Company B'],
            'crate_type': ['Plastic', 'Wood', 'Plastic', 'Metal', 'Plastic']
        }
        self.df = pd.DataFrame(data)

    ## Test assert equal
    def test_crate_distribution_ok(self):
        expected_output = pd.DataFrame({
            'company_name': ['Company A', 'Company A', 'Company A', 'Company B'],
            'crate_type': ['Metal', 'Plastic', 'Wood', 'Plastic'],
            'order_count': [1, 1, 1, 2]
        })
        result = crate_distribution(self.df)
        print(result)

        pd.testing.assert_frame_equal(result, expected_output)

    ## Test assert non equal
    def test_crate_distribution_ko(self):
        expected_output = pd.DataFrame({
            'company_name': ['Company A', 'Company A', 'Company B'],
            'crate_type': ['Metal', 'Plastic', 'Plastic'],
            'order_count': [1, 1, 2]
        })
        result = crate_distribution(self.df)
        print(result)

        ## Try to evaluate assert condition, if it's equal it must fail otherwise the test has been successful
        try:
            pd.testing.assert_frame_equal(result, expected_output)
            raise AssertionError("Equal dataframes, test not passed")
        except AssertionError:
            print("Different dataframes, test passed")

if __name__ == '__main__':
    unittest.main()