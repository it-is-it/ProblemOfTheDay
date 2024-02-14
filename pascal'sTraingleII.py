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

from typing import List  # Importing List class from the typing module

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:  # Define a method named getRow
                                                  # Takes an integer rowIndex as input
                                                  # Returns a list of integers
        triangle = []  # Initialize an empty list to store rows of Pascal's triangle
        
        # Loop through each row index from 0 to rowIndex (inclusive)
        for i in range(rowIndex + 1):
            # Initialize a list 'row' with 'None' values for the current row
            row = [None] * (i + 1)
            
            # Set the first and last elements of 'row' to 1 (edge elements of Pascal's triangle)
            row[0], row[-1] = 1, 1
            
            # Loop through each element of 'row' except the edge elements
            for j in range(1, len(row) - 1):
                # Calculate the value of the current element using values from the previous row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            # Append the current row to the triangle list
            triangle.append(row)
        
        # Return the row of Pascal's triangle specified by rowIndex
        return triangle[rowIndex]

solution = Solution()  # Create an instance of the Solution class

# Test the getRow method with different row indices and print the results
print(solution.getRow(3))
print(solution.getRow(0))
print(solution.getRow(1))
