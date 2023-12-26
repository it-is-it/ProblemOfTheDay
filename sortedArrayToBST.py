# 108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # Find the middle index
        mid = len(nums) // 2

        # Create the root node with the middle element
        root = TreeNode(nums[mid])

        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

    def printTree(self,root):
        if root:
            self.printTree(root.left)
            print(root.val, end=' ')
            self.printTree(root.right)

# Example usage:
solution = Solution()
nums1 = [-10, -3, 0, 5, 9]
tree1 = solution.sortedArrayToBST(nums1)
solution.printTree(tree1)
# Output: -10 -3 0 5 9

nums2 = [1, 3]
tree2 = solution.sortedArrayToBST(nums2)
solution.printTree(tree2)
# Output: 1 3
