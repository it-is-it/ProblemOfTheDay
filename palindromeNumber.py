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

class Solution:
    def isPalindrome(self,x:int)->bool:
        # if x < 0:
        #     return False
        # original = x
        # reverse = 0
        # while x > 0:
        #     digit = x % 10;
        #     reverse = reverse * 10 + digit
        #     x //= 10
        # if reverse == original:
        #     return True


        # Handle negative numbers
        if x < 0:
            return False
        
        # Convert the integer to a string
        x_str = str(x)
        
        # Check if the string is the same as its reverse
        return x_str == x_str[::-1]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Palindrome number
    result1 = solution.isPalindrome(121)
    print(f"121 is a palindrome: {result1}")  # Expected output: True
    
    # Test case 2: Non-palindrome number
    result2 = solution.isPalindrome(-121)
    print(f"-121 is a palindrome: {result2}")  # Expected output: False
    
    # Test case 3: Single-digit number
    result3 = solution.isPalindrome(10)
    print(f"5 is a palindrome: {result3}")  # Expected output: False
