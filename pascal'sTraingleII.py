# 119. Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle =[]
        for i in range(rowIndex+1):
            row=[None for _ in range(i+1)]
            row[0],row[-1]=1,1
            for j in range(1, len(row)-1):
                row[j]= triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle[rowIndex-1]

solution= Solution()
print(solution.getRow(3))