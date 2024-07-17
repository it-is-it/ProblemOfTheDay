# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# output: 21 
class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of the input number
        sign = -1 if x < 0 else 1
        
        # Make x positive for easier manipulation
        x *= sign
        
        # Initialize the reversed number to 0
        rev = 0
        
        # Reverse the digits of the number
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        
        # Reapply the sign to the reversed number
        rev *= sign
        
        # Check for overflow (32-bit signed integer range)
       

        
        # Check for overflow (32-bit signed integer range)
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

solution = Solution()
print(solution.reverse(123))    # Output: 321
print(solution.reverse(-123))   # Output: -321
print(solution.reverse(120))    # Output: 21
print(solution.reverse(-1563847412))  # Output: 0
