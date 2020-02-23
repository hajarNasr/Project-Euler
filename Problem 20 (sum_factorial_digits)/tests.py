import unittest
from twenty import sum_factorial_digits

class TestSumFactorialDigits(unittest.TestCase):
    def test_sum_factorial_digits(self):
        self.assertEqual(sum_factorial_digits(10), 27)
        self.assertEqual(sum_factorial_digits(25),72)
        self.assertEqual(sum_factorial_digits(50), 216)
        self.assertEqual(sum_factorial_digits(75), 432)
        self.assertEqual(sum_factorial_digits(100), 648)


if __name__ == '__main__':
    unittest.main()  