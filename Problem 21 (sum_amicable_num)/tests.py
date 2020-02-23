import unittest 
from twentyOne import sum_amicable_num

class TestSumAmicableNum(unittest.TestCase):
    def test_sum_amicable_num(self):      
        self.assertEqual(sum_amicable_num(1000),504)
        self.assertEqual(sum_amicable_num(2000),2898)
        self.assertEqual(sum_amicable_num(5000),8442)
        self.assertEqual(sum_amicable_num(10000),31626)

if __name__ == '__main__':
    unittest.main()          