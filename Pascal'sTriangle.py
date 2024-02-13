# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1  # First and last element of each row is always 1
            for j in range(1, len(row)-1):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

# Example usage
sol = Solution()
result = sol.generate(5)
for row in result:
    print(row)

