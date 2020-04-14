import unittest
from smallest_difference import SmallestDifference

class SmallestDifferenceTest(unittest.TestCase):
    def setUp(self):
        self.smallest_diff = SmallestDifference()
    
    def tearDown(self):
        del self.smallest_diff

    def test_two_arrays_with_positive_integers(self):
        self.assertEqual(self.smallest_diff.smallest_difference([3,6], [1,4]), [3,4])
        
if __name__ == "__main__":
    unittest.main()