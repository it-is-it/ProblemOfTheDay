# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# class Solution:
#     def isPalindrome(self,x:int)->bool:
#         # if x < 0:
#         #     return False
#         # original = x
#         # reverse = 0
#         # while x > 0:
#         #     digit = x % 10;
#         #     reverse = reverse * 10 + digit
#         #     x //= 10
#         # if reverse == original:
#         #     return True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers
        if x < 0:
            return False

        # Convert the integer to a string
        x_str = str(x)
        
        # Get the length of the string
        n = len(x_str)
        
        # Iterate through the first half of the string
        for i in range(n // 2):
            # Compare characters from the beginning and end of the string
            if x_str[i] != x_str[n - i - 1]:
                return False
        
        # If no non-matching characters were found, it's a palindrome
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))  # True (121 is a palindrome)
    print(solution.isPalindrome(-121)) # False (negative numbers can't be palindromes)
    print(solution.isPalindrome(10))   # False (10 is not a palindrome)
