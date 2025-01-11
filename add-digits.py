# 258. Add Digits
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0


class Solution:
    def addDigits(self, num: int) -> int:
        # result = 0
        # while len(str(num)) > 1:
        #     result = 0
        #     while num > 0: 
        #         remainder = num % 10
        #         result += remainder
        #     num = result
        # return num
        if num == 0:
           return 0
        return 1 + (num - 1) % 9



solution = Solution()

# Test Case 1
n1 = 38  
print("Test Case 1:")
print("Input:", n1)
print("Output:", solution.addDigits(n1))  

# Test Case 2
n2 = 0 
print("Test Case 2:")
print("Input:", n2)
print("Output:", solution.addDigits(n2))  