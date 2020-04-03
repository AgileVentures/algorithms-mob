# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4


class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        from collections import defaultdict
        count_of_numbers = defaultdict(int)
        for i in nums:
            count_of_numbers[i] += 1
        for k in count_of_numbers.keys():
            if count_of_numbers[k] == 1:
                return k
        return

s = Solution()
s.singleNumber([4,1,2,1,2]) # 4
s.singleNumber([2,1,2]) # 1
