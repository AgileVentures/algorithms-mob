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
        
        for i in range(len(array)):
            diff = total_sum - array[i]
            if diff in array[:i] or diff in array[i+1:]:
                return [array[i], diff]
        return []