# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Importing the 'Optional' type for better type hints
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Constructor for the TreeNode class, initializing node with value 'val' and left/right children.
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Method to check if a tree is symmetric, takes the root of the tree as input.
        if not root:
            # If the root is None, the tree is symmetric.
            return True
        return self.isMirror(root.left, root.right)
        # Otherwise, delegate the comparison to the isMirror method.

    def isMirror(self, left, right) -> bool:
        # Helper method to check if two subtrees are mirror images of each other.
        if not left and not right:
            # If both nodes are None, they are mirror images.
            return True
        elif not left or not right:
            # If one of the nodes is None and the other is not, they are not mirror images.
            return False
        elif left.val != right.val:
            # If the values of the nodes are different, they are not mirror images.
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        # Recursively check if the left subtree of the left child is the mirror image of the right subtree
        # of the right child, and vice versa.

# Example 1
root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
# Creating the first example binary tree.
sol = Solution()
# Creating an instance of the Solution class.
result1 = sol.isSymmetric(root1)
# Checking if the first tree is symmetric using the isSymmetric method.
print(result1)  # Output: True
# Printing the result.

# Example 2
root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
# Creating the second example binary tree.
result2 = sol.isSymmetric(root2)
# Checking if the second tree is symmetric using the isSymmetric method.
print(result2)  # Output: False
# Printing the result.
