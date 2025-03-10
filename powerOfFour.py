# 342. Power of Four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

# Example 1:
# Input: n = 16
# Output: true

# Example 2:
# Input: n = 5
# Output: false

# Example 3:
# Input: n = 1
# Output: true
 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1

# Creating an instance of the Solution class
solution = Solution()

# Test cases
test_cases = {
    "Example 1": 16,
    "Example 2": 5,
    "Example 3": 1,
}

# Running the test cases and collecting results
results = {name: solution.isPowerOfFour(n) for name, n in test_cases.items()}
results
