# 263. Ugly Number
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

# Example 1:
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.

# Example 3:
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:  # Negative numbers and zero are not considered "ugly"
            return False
        for factor in [2, 3, 5]:  # Check for factors 2, 3, and 5
            while n % factor == 0:  # Keep dividing n by the factor as long as it's divisible
                n //= factor
        return n == 1  # If the final n is 1, it's an ugly number


    
solution = Solution()
print(solution.isUgly(6))
print(solution.isUgly(1))
print(solution.isUgly(14))