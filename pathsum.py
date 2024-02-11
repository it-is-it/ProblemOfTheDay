from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Check if the current node is a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# Constructing the binary tree
#      1
#     / \
#    2   3
    
root = TreeNode(1, TreeNode(2, 3))

# Creating an instance of the solution class
solution = Solution()

# Calling the hasPathSum method and storing the result
result = solution.hasPathSum(root, 5)

print(result)  # Output: True
