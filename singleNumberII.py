# 137. Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3

# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

from typing import List

class Solution:
    def singleNumberII(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # Update twos to store bits that appear twice
            twos |= ones & num
            # Update ones to store bits that appear once
            ones ^= num
            # Calculate common bits that appear three times
            common_bit_mask = ~(ones & twos)
            # Clear bits in ones and twos where the corresponding bit is set in common_bit_mask
            ones &= common_bit_mask
            twos &= common_bit_mask
        # The remaining bits in ones represent the single element
        return ones

# Test cases
sol = Solution()
print(sol.singleNumberII([2,2,3,2]))         # Output: 3
print(sol.singleNumberII([0,1,0,1,0,1,99]))  # Output: 99
