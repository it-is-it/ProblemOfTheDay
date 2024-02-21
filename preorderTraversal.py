# 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.preorderRecursive(root, result)
        return result

    def preorderRecursive(self, node, result):
        if node:
            result.append(node.val)  # Visit the node
            self.preorderRecursive(node.left, result)  # Traverse left subtree
            self.preorderRecursive(node.right, result)  # Traverse right subtree


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.preorderTraversal(root))  # Output: [1, 2, 3]

