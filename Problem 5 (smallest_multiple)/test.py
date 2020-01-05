import unittest
from five import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
      
      def test_smallest_multiple(self):
          data = [5, 7, 10]
          results = [60, 420, 2520]
          self.assert_loop(data, results)

      def test_smallest_multiple_for_large_numbers(self):
          data = [13, 20] 
          results = [360360, 232792560]  
          self.assert_loop(data, results)   

      def assert_loop(self, data, results): 
          for i in range(len(data)):
              self.assertEqual(smallest_multiple(data[i]), results[i]) 

      def test_worng_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
           result = smallest_multiple(data)
        

if __name__ == '__main__':
    unittest.main()    
