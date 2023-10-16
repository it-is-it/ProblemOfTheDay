# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        # Define strings for opening and closing brackets
        opening_brackets = "({["
        closing_brackets = ")}]"

        # Iterate through each character in the input string
        for char in s:
            # If the character is an opening bracket
            if char in opening_brackets:
                # Push the opening bracket onto the stack
                stack.append(char)
            # If the character is a closing bracket
            elif char in closing_brackets:
                # Check if the stack is empty or if the top of the stack corresponds to the current closing bracket
                if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                    # Mismatched brackets, return False
                    return False

        # If the stack is empty, all opening brackets were properly closed, return True
        # Otherwise, there are unmatched opening brackets, return False
        return len(stack) == 0

# Test cases
solution = Solution()
print(solution.isValid("()"))  # Output: True (properly closed)
print(solution.isValid("()[]{}"))  # Output: True (properly closed)
print(solution.isValid("(]"))  # Output: False (mismatched brackets)
print(solution.isValid("([)]"))  # Output: False (mismatched brackets)
print(solution.isValid("{[]}"))  # Output: True (properly closed)
