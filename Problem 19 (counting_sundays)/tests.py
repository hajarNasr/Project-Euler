import unittest
from nineteen import counting_sundays

class CountingSundays(unittest.TestCase):
     def test_counting_sundays(self):
         self.assertEqual(counting_sundays(1943, 1946), 6)
         self.assertEqual(counting_sundays(1995, 2000), 10)
         self.assertEqual(counting_sundays(1901, 2000), 171)

if __name__ == '__main__':
    unittest.main()