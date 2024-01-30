# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  # Not balanced
            return 1 + max(left_height, right_height)

        return height(root) != -1


# Example usage:
# Construct the tree for Example 1
root_example1 = TreeNode(3)
root_example1.left = TreeNode(9)
root_example1.right = TreeNode(20)
root_example1.right.left = TreeNode(15)
root_example1.right.right = TreeNode(7)

# Check if the tree is balanced
solution = Solution()
output_example1 = solution.isBalanced(root_example1)
print(output_example1)  # Output: True
