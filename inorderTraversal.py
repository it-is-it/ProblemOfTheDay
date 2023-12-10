# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Constructor for TreeNode class
        self.val = val         # Value of the current node
        self.left = left       # Reference to the left child node
        self.right = right     # Reference to the right child node

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Function to perform inorder traversal and return the result as a list
        result = []  # Initialize an empty list to store the result
        self.inorderTraversalRecursive(root, result)  # Call the recursive helper function
        return result  # Return the final result list

    def inorderTraversalRecursive(self, node, result):
        # Helper function for recursive inorder traversal
        if node:
            # If the current node is not None
            # Traverse the left subtree
            self.inorderTraversalRecursive(node.left, result)
            
            # Visit the current node
            result.append(node.val)
            
            # Traverse the right subtree
            self.inorderTraversalRecursive(node.right, result)

# Construct a sample binary tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create a Solution instance and perform inorder traversal
solution = Solution()
result = solution.inorderTraversal(root)

print(result)  # Output: [1, 3, 2]
