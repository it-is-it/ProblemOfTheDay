# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:\
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = ["h", "e", "l", "l", "o"]
    solution.reverseString(s1)
    print("Output for Test Case 1:", s1)  # Expected: ["o", "l", "l", "e", "h"]
    
    # Test case 2
    s2 = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s2)
    print("Output for Test Case 2:", s2)  # Expected: ["h", "a", "n", "n", "a", "H"]
    
    # Test case 3 (single character)
    s3 = ["a"]
    solution.reverseString(s3)
    print("Output for Test Case 3:", s3)  # Expected: ["a"]
    
    # Test case 4 (empty list)
    s4 = []
    solution.reverseString(s4)
    print("Output for Test Case 4:", s4)  # Expected: []
    
    # Test case 5 (palindrome)
    s5 = ["r", "a", "c", "e", "c", "a", "r"]
    solution.reverseString(s5)
    print("Output for Test Case 5:", s5)  # Expected: ["r", "a", "c", "e", "c", "a", "r"]
