import unittest
from four import largest_palindrome_product

class TestLargestPalindromeProuct(unittest.TestCase):
    
    def test_largest_palindrome_product_two_digit_numbers(self):
        result = largest_palindrome_product(2)
        self.assertEqual(result, 9009)

    def test_largest_palindrome_product_three_digit_numbers(self):
        result = largest_palindrome_product(3)
        self.assertEqual(result, 906609)

    def test_worng_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
           result = largest_palindrome_product(data)

if __name__ == '__main__':
    unittest.main()    

