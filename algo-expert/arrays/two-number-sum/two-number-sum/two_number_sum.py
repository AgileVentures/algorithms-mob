#  write a function that takes a non-empty array of distinct integers
# and an integer representing a target sum. If any two number in the input array adds up to the target sum,
# the function should return them in an array, in any order.
# If no two numbers sum up to the target sum, the function should return an empty array.
# You can assume that there will be at most one pair of numbers that add up to the target sum.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
class TwoNumberSum:
    def __init__(self):
        pass
    def get_two_sum_with_n_squared_time(self, array, total_sum):
        """
            Time complexit o(n^2)
            space complexity o(1)
        """

        for i in range(len(array)):
            diff = total_sum - array[i]
            if diff in array[:i] or diff in array[i+1:]:
                return [array[i], diff]
        return []

    def get_two_sum_using_a_dict(self, array, total_sum):
        """
            time complexity o(n)
            space complexity o(n)
        """
        lookup_dict = {}

        for i in array:
            diff = total_sum - i
            if diff in lookup_dict:
                return [i, diff]
            else:
                lookup_dict[i] = True
        return []

    def get_two_sum_by_first_sorting_list(self, array, total_sum):
        """
            Time complexity o(n log n)
            space complexity o(1)
        """
        array.sort()
        start_index = 0
        end_index = len(array) - 1

        while end_index > start_index:
            current_sum = array[start_index] + array[end_index]

            if current_sum > total_sum:
                end_index -= 1
            elif current_sum < total_sum:
                start_index += 1
            else:
                return [array[start_index], array[end_index]]
        return []
        