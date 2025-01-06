# 303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
# Example 1:
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # Initialize the object with the array of integers
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of the elements between left and right indices (inclusive)
        total = sum(self.nums[left:right + 1])  # Use slicing to get the range
        return total

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
obj = NumArray(nums)

# Sum of elements between indices 1 and 4 (i.e., 2 + 3 + 4 + 5)
print(obj.sumRange(1, 4))  # Output: 14

# Sum of elements between indices 0 and 2 (i.e., 1 + 2 + 3)
print(obj.sumRange(0, 2))  # Output: 6
