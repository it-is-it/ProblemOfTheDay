# 145. Binary Tree Postorder Traversal

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]
 
# Constraints:
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.postorderRecursive(root, result)
        return result

    def postorderRecursive(self, node, result):
        if node:
            self.postorderRecursive(node.left, result)  # Traverse left subtree
            self.postorderRecursive(node.right, result)  # Traverse right subtree
            result.append(node.val)  # Visit the node


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root))  # Output: [1, 2, 3]

