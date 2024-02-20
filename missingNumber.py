# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sort the input list
        nums.sort()
        
        # Initialize a variable to store the expected number
        expected_num = 0
        
        # Iterate through the sorted list
        for num in nums:
            # If the current number is not equal to the expected number, it's the missing number
            if num != expected_num:
                return expected_num
            # Increment the expected number for the next iteration
            expected_num += 1
        
        # If no missing number is found, return the next expected number
        return expected_num

# Test the solution
sol = Solution()
print(sol.missingNumber([3, 0, 1]))  # Output: 2
print(sol.missingNumber([0, 1]))  # Output: 2
print(sol.missingNumber([9,6,4,2,3,5,7,0, 1]))  # Output: 8
