# 191. Number of 1 Bits
# Given a positive integer n, write a function that returns the number of 
# set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

# Create an instance of the Solution class
solution = Solution()

# Test Case 1
n1 = 11  # Binary: 1011
print("Test Case 1:")
print("Input:", n1)
print("Output:", solution.hammingWeight(n1))  # Expected Output: 3

# Test Case 2
n2 = 128  # Binary: 10000000
print("\nTest Case 2:")
print("Input:", n2)
print("Output:", solution.hammingWeight(n2))  # Expected Output: 1

# Test Case 3
n3 = 2147483645  # Binary: 1111111111111111111111111111101
print("\nTest Case 3:")
print("Input:", n3)
print("Output:", solution.hammingWeight(n3))  # Expected Output: 30
