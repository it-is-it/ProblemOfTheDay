# 912. Sort an Array

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.

 #Implementing mergesort in this method of sorting an array
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: if the array has 0 or 1 element, it is already sorted.
        if len(nums) <= 1:
            return nums

        # Find the middle index to divide the array into two halves.
        mid = len(nums) // 2

        # Split the array into left and right halves.
        L = nums[:mid]
        R = nums[mid:]

        # Recursively sort both halves.
        L = self.sortArray(L)
        R = self.sortArray(R)

        # Initialize pointers for merging.
        i = j = k = 0

        # Merge the two sorted halves back together.
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        # Check if any elements were left in the left and right halves.
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1

        return nums

# Test cases
solution = Solution()

# Test case 1: Sorting a list with multiple elements.
input1 = [5,2,3,1]
sorted_input1 = solution.sortArray(input1)
print(sorted_input1)  # Output: [1,2,3,5]

# Test case 2: Sorting a list with duplicate elements.
input2 = [5,1,1,2,0,0]
sorted_input2 = solution.sortArray(input2)
print(sorted_input2)  # Output: [0,0,1,1,2,5]