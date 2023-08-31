#leetcode 1389
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:

# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

# It is guaranteed that the insertion operations will be valid.

 

# Example 1:

# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]
# Example 2:

# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]
# Example 3:

# Input: nums = [1], index = [0]
# Output: [1]

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Create an empty list to put the cards in the right order
        arr = []

        # Go through each card and its special instruction
        for n, i in zip(nums, index): 
            # Create a special spot for the card at the place the instruction says
            # It's like finding the right place for a toy in a row
            # The card will be all alone at that spot
            arr[i:i] = [n]

        # After all the cards are in their spots, the row is ready!
        return arr

# Example usage
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
solution = Solution()
result = solution.createTargetArray(nums, index)
print(result)  # Output: [0, 4, 1, 3, 2]
