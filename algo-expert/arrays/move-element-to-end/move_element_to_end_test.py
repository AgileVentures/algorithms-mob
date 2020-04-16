import unittest
from move_element_to_end import MoveElementToEnd

class MoveElementToEndTest(unittest.TestCase):
    
    def setUp(self):
        self.move_element = MoveElementToEnd()
    
    def tearDown(self):
        del self.move_element

    def first_test(self):
        print("here")
        self.assertEqual(self.move_element.move_element_to_ends([2, 1, 2, 2, 2, 3, 4, 2], 2), [ 1, 3, 4, 2, 2, 2, 2, 2])

if __name__ == "__main__":
    unittest.main()
