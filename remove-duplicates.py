from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        non_duplicate_ptr = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[non_duplicate_ptr]:
                non_duplicate_ptr += 1
                nums[non_duplicate_ptr] = nums[i]
        
        return non_duplicate_ptr + 1

# Test cases
sol = Solution()

# Test Case 1
nums1 = [1, 1, 2]
result1 = sol.removeDuplicates(nums1)
print("Test Case 1 - Result:", result1)  # Expected Output: 2, after removing duplicates [1, 2]

# Test Case 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = sol.removeDuplicates(nums2)
print("Test Case 2 - Result:", result2)  # Expected Output: 5, after removing duplicates [0, 1, 2, 3, 4]
