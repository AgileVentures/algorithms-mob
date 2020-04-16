import unittest
from two_number_sum import TwoNumberSum

class TestTwoNumberSum(unittest.TestCase):
    def setUp(self) -> None:
        self.test_two_number = TwoNumberSum()
    def tearDown(self):
        del self.test_two_number

    def test_two_positive_integers_with_elements_that_sum(self):
        array = [1,2]
        total_sum = 3
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time(array, total_sum))
        self.assertEqual( output,[1,2])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict(array, total_sum))
        self.assertEqual( output2,[1,2])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list(array, total_sum))
        self.assertEqual( output3,[1,2])
    
    def test_three_positive_integer_with_elements_that_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([4, 6, 1], 5))
        self.assertEqual(output, [1, 4])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([4, 6, 1], 5))
        self.assertEqual(output2, [1, 4])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([4, 6, 1], 5))
        self.assertEqual(output3, [1, 4])

    def test_integers_with_elements_that_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([4, 6, 1, -3], 3))
        self.assertEqual(output, [-3, 6])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([4, 6, 1, -3], 3))
        self.assertEqual(output2, [-3, 6])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([4, 6, 1, -3], 3))
        self.assertEqual(output3, [-3, 6])

    def test_integers_with_a_number_that_if_doubled_gives_the_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual(output, [-1, 11])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual(output2, [-1, 11])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual(output3, [-1, 11])
    

    def test_sorted_integers_with_elemets_that_add_up_to_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
        self.assertEqual(output, [8, 9])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
        self.assertEqual(output2, [8, 9])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
        self.assertEqual(output3, [8, 9])
    
    def test_larger_sorted_integers_with_elemets_that_add_up_to_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
        self.assertEqual(output, [3, 15])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
        self.assertEqual(output2, [3, 15])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
        self.assertEqual(output3, [3, 15])

    def test_larger_sorted_integers_with_negatives_with_elemets_that_add_up_to_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))
        self.assertEqual(output, [-5, 0])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))
        self.assertEqual(output2, [-5, 0])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))
        self.assertEqual(output3, [-5, 0])

    def test_larger_sorted_integers_with_larger_elemets_that_add_up_to_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
        self.assertEqual(output, [-47, 210])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
        self.assertEqual(output2, [-47, 210])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
        self.assertEqual(output3, [-47, 210])

    def test_unsorted_integers_without_elemets_that_add_up_to_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
        self.assertEqual(output, [])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
        self.assertEqual(output2, [])

        output3 = sorted(self.test_two_number.get_two_sum_by_first_sorting_list([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
        self.assertEqual(output3, [])

    def test_integers_without_elemets_that_add_up_to_sum(self):
        output = sorted(self.test_two_number.get_two_sum_with_n_squared_time([3, 5, -4, 8, 11, 1, -1, 6], 15))
        self.assertEqual(output, [])

        output2 = sorted(self.test_two_number.get_two_sum_using_a_dict([3, 5, -4, 8, 11, 1, -1, 6], 15))
        self.assertEqual(output2, [])

        output3= sorted(self.test_two_number.get_two_sum_by_first_sorting_list([3, 5, -4, 8, 11, 1, -1, 6], 15))
        self.assertEqual(output3, [])
    

if __name__ == "__main__":
    unittest.main()