# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1 

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the count of each number
        num_count = {}
        
        # Count occurrences of each number in the list
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        # Find the number with only one occurrence
        for num, count in num_count.items():
            if count == 1:
                return num

# Test cases
sol = Solution()
print(sol.singleNumber([2, 2, 1]))  # Output: 1
print(sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
print(sol.singleNumber([1]))  # Output: 1
