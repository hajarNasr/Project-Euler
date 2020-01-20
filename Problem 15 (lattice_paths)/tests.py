import unittest
from fifteen import lattice_paths

class LatticePaths(unittest.TestCase):
    def test_lattice_paths(self):
        self.assertEqual(lattice_paths(4), 70)
        self.assertEqual(lattice_paths(9), 48620)
        self.assertEqual(lattice_paths(20), 137846528820)

if __name__ == '__main__':
    unittest.main()        