import unittest
from eight import largest_productina_series

class LargestProductinaSeries(unittest.TestCase):

    def test_largest_productina_series(self):
        self.assertEqual(largest_productina_series(4), 5832) 
        self.assertEqual(largest_productina_series(13), 23514624000)

if __name__ == '__main__':
    unittest.main()            