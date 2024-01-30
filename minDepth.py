# 111. Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # If one of the subtrees is empty, consider the non-empty subtree
        if not left_depth or not right_depth:
            return 1 + left_depth + right_depth

        return 1 + min(left_depth, right_depth)

# Create the tree from the serialized input
root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))


# Instantiate the Solution class and call minDepth method
solution = Solution()
result = solution.minDepth(root)

# Print the result
print("Minimum Depth:", result)

