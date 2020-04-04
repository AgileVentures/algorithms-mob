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
    def singleNumber(self, nums) -> int: 
        from collections import defaultdict
        count_of_numbers = defaultdict(int)
        for i in nums:
            count_of_numbers[i] += 1
        for k in count_of_numbers.keys():
            if count_of_numbers[k] == 1:
                return k
        return
    
    def singleNumberAsSet(self, nums) -> int:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                nums_set.remove(i)
            else:
                nums_set.add(i)
        return nums_set.pop()
    
    def singleNumberWithXOR(self, nums) -> int:
        """
            Memory complexty o(1)
            Time complexity o(n)
            uses xor
        """
        result = 0
        for i in nums:
            result ^= i
        return result

s = Solution()
print(s.singleNumber([4,1,2,1,2])) # 4
print(s.singleNumber([2,1,2])) # 1
print(s.singleNumberAsSet([4,1,2,1,2])) # 4
print(s.singleNumberAsSet([2,1,2])) # 1
print(s.singleNumberWithXOR([4,1,2,1,2])) # 4
print(s.singleNumberWithXOR([2,1,2])) # 1
