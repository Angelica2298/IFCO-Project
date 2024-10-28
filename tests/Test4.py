from collections import defaultdict
import os
import sys
import unittest
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.Exercise4 import get_commissions

class TestCommissionCalculation(unittest.TestCase):
    def setUp(self):
        # Data for tests
        self.df_test = pd.DataFrame({
            'order_id': [1, 2, 3],
            'grossValue': [10000, 20000, 30000],  # euros
            'salesowners': [
                "David Goliat, Leonard Cohen, Luke Skywalker",
                "David Goliat, David Henderson",
                "David Henderson, Leonard Cohen, David Goliat, Luke Skywalker"
            ]
        })
    
    def test_commission_calculation(self):
        # Simulated data for test
        expected_commissions = {
            'David Goliat': 2085.0,   # Main owner orders 1 and 2, co-owner order 3
            'Leonard Cohen': 1000.0,      # Co-owner orders 1 and 3
            'Luke Skywalker': 95.0,   # Co-owner orders 1 and 3
            'David Henderson': 2300.0      # Main owner order 3, co-owner order 2
        }
        total_commissions = defaultdict(float)

        # Replicate the logic from exercise to get the dictioinary with calculated commissions
        for _, row in self.df_test.iterrows():
            commissions = get_commissions(row)
            print(commissions)
            for owner, commission in commissions.items():
                total_commissions[owner] += commission
        
        print(total_commissions)

        for owner, commission in expected_commissions.items():
            self.assertAlmostEqual(total_commissions[owner], commission, places=2)

if __name__ == '__main__':
    unittest.main()