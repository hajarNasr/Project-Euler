import unittest
from seven import nth_prime

class TestNthPrime(unittest.TestCase):

    def test_nth_prime_for_small_numbers(self):
        data = [6, 10, 100]
        results = [13, 29, 541]
        self.assert_loop(data, results)

    def test_nth_prime_for_big_numbers(self):
        data = [1000, 10001] 
        results = [7919, 104743]  
        self.assert_loop(data, results)   

    def assert_loop(self, data, results): 
        for i in range(len(data)):
            self.assertEqual(nth_prime(data[i]), results[i])     

if __name__ == '__main__':
    unittest.main()    
