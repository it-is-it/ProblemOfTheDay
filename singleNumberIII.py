# 260. Single Number III
# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

# Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]

# Example 3:
# Input: nums = [0,1]
# Output: [1,0]

from typing import List

class Solution:
    def singleNumberIII(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get XOR of the two single numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Step 2: Find the rightmost set bit
        rightmost_set_bit = xor_result & -xor_result
        
        # Step 3: Divide numbers into two groups based on the rightmost set bit
        single_numbers = [0, 0]
        for num in nums:
            if num & rightmost_set_bit:
                single_numbers[0] ^= num
            else:
                single_numbers[1] ^= num
        
        return single_numbers

# Test cases
sol = Solution()
print(sol.singleNumberIII([1,2,1,3,2,5]))  # Output: [3, 5]
print(sol.singleNumberIII([-1,0]))          # Output: [-1, 0]
print(sol.singleNumberIII([0,1]))           # Output: [0, 1]

