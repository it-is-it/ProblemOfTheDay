# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        for index in range(len(nums)):
            if nums[index] >= target:
                return index
        # If the target is greater than all elements in nums, insert it at the end
        return len(nums)

# Example usage
solution = Solution()
nums1 = [1, 3, 5, 6]
target1 = 2
print(solution.searchInsert(nums1, target1))  # Output: 1

nums2 = [1, 3, 5, 6]
target2 = 5
print(solution.searchInsert(nums2, target2)) # Output: 2

nums3 = [1, 3, 5, 6]
target3 = 7
print(solution.searchInsert(nums3, target3))  # Output: 4