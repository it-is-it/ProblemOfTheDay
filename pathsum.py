# 112. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

from typing import Optional

# Definition of TreeNode class representing a node in a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Constructor to initialize a TreeNode instance with a value and optional left and right children
        self.val = val  # Assigns the value of the node
        self.left = left  # Assigns the left child of the node
        self.right = right  # Assigns the right child of the node

# Definition of Solution class containing the hasPathSum method
class Solution:
    # Method to check if there exists a path in the binary tree from root to leaf node such that the sum of node values equals the targetSum
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            # If root is None, return False since there is no path
            return False
        
        # Check if the current node is a leaf node
        if not root.left and not root.right:
            # If the current node is a leaf node, check if the value of the leaf node equals targetSum
            return targetSum == root.val
        
        # Recursively check the left and right subtrees
        # Subtract the value of the current node from targetSum and check if the remaining targetSum can be obtained by any path in the subtree
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)



# Example 1
# Constructing the binary tree
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \      \
# 7   2      1
root1 = TreeNode(5)
root1.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root1.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
targetSum1 = 22

# Example 2
# Constructing the binary tree
#      1
#     / \
#    2   3
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
targetSum2 = 5

# Example 3
# Constructing an empty binary tree (root is None)
root3 = None
targetSum3 = 0

# Create an instance of the Solution class
solution = Solution()

# Perform tests
# Checking if there exists a path from the root to a leaf node such that the sum of node values along the path equals the target sum
print(solution.hasPathSum(root1, targetSum1))  # Output: True
print(solution.hasPathSum(root2, targetSum2))  # Output: False
print(solution.hasPathSum(root3, targetSum3))  # Output: False
