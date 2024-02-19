# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome. 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize an empty string to store cleaned version of the input string
        cleaned_string = ''
        
        # Iterate through each character in the input string
        for char in s:
            # Check if the character is alphanumeric
            if char.isalnum():  
                # Convert the character to lowercase and add it to the cleaned string
                cleaned_string += char.lower()
        
        # Reverse the cleaned string
        reversed_string = cleaned_string[::-1]
        
        # Check if the reversed string is equal to the cleaned string
        return reversed_string == cleaned_string

def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        "A man, a plan, a canal: Panama",  # Palindrome
        "race a car",                      # Not a palindrome
        " "                                # Palindrome
    ]
    
    # Iterate over test cases
    for test_case in test_cases:
        # Call the isPalindrome method and print the result
        print(f"'{test_case}' is a palindrome: {solution.isPalindrome(test_case)}")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
