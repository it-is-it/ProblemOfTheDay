
# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a,2)
        b1 = int(b,2)
        result = a1 + b1
        return bin(result)[2:]
    
solution = Solution()
print(solution.addBinary("11", "1"))
print(solution.addBinary("1010", "1011"))