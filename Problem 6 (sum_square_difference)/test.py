import unittest
from six import sum_square_difference

class TestSumSquareDifference(unittest.TestCase):
    
    def test_sum_square_difference(self):
        data = [10, 20, 100]
        results = [2640, 41230, 25164150]
        for i in range(len(data)):
            self.assertEqual(sum_square_difference(data[i]), results[i]) 

    def test_worng_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
           result = sum_square_difference(data)  

if __name__ == '__main__':
    unittest.main()    
