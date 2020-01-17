import unittest
from twelve import divisible_triangle_number

class DivisibleTriangleNumber(unittest.TestCase):
    def test_divisible_triangle_number(self):
        self.assertEqual(divisible_triangle_number(5),28)
        self.assertEqual(divisible_triangle_number(23),630)
        self.assertEqual(divisible_triangle_number(167),1385280)
        self.assertEqual(divisible_triangle_number(374),17907120)
        self.assertEqual(divisible_triangle_number(500),76576500)

if __name__ == '__main__':
    unittest.main()         