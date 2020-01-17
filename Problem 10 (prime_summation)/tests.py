import unittest
from ten import prime_summation

class PrimeSummation(unittest.TestCase):

    def test_prime_summation(self):
       self.assertEqual(prime_summation(17), 41)
       self.assertEqual(prime_summation(2001), 277050)

if __name__ == '__main__':
    unittest.main()     