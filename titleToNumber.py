# 171. Excel Sheet Column Number
# Easy
# Topics
# Companies
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, letter in enumerate(columnTitle):
            # Convert the letter to a number and adjust its position
            result = result * 26 + (ord(letter) - ord('A') + 1)
        return result


# Test the solution
solution = Solution()
print(solution.titleToNumber("A"))       # Output: 1
print(solution.titleToNumber("Z"))       # Output: 26
print(solution.titleToNumber("AA"))      # Output: 27
print(solution.titleToNumber("AB"))      # Output: 28
print(solution.titleToNumber("AAA"))     # Output: 703
