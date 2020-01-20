from fourteen import longest_collatz_sequence
import unittest

class LongestCollatzSequence(unittest.TestCase):
    def test_longest_collatz_sequence(self):
        self.assertEqual(longest_collatz_sequence(14),9)
        self.assertEqual(longest_collatz_sequence(5847),3711)
        self.assertEqual(longest_collatz_sequence(46500),35655)
        self.assertEqual(longest_collatz_sequence(54512),52527)
        self.assertEqual(longest_collatz_sequence(100000),77031)

if __name__ == '__main__':
    unittest.main()        