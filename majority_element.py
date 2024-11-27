# 169. Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List  # Import List for type hints

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in the list `nums`.
        A majority element is the one that appears more than `len(nums) // 2` times.
        """
        result_dict = {}  # Dictionary to store the frequency of each number
        
        # Count the occurrences of each number
        for num in nums:
            result_dict[num] = result_dict.get(num, 0) + 1
        
        # Calculate the threshold for a majority element
        majority_count = len(nums) // 2
        
        # Find the element with a frequency greater than the majority count
        for key, value in result_dict.items():
            if value > majority_count:
                return key  # Return the majority element when found

# Create an instance of the Solution class
solution = Solution()

# Test case 1
list1 = [3, 2, 3]
print(solution.majorityElement(list1))  # Output: 3

# Test case 2
list2 = [2, 2, 1, 1, 1, 2, 2]
print(solution.majorityElement(list2))  # Output: 2
