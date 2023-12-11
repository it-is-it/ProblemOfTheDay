# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are equal
        if not p and not q:
            return True
        # If one of the nodes is None and the other is not, they are not equal
        elif not p or not q:
            return False
        # If the values of the current nodes are not equal, the trees are not the same
        elif p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

solution = Solution()
print(solution.isSameTree(p1, q1))  # Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false
p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)

print(solution.isSameTree(p2, q2))  # Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)

q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)

print(solution.isSameTree(p3, q3))  # Output: false
