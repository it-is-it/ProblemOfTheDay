# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty, return an empty string
        if not strs:
            return ""
        
        # Iterate through the characters of the first string
        for index, char in enumerate(strs[0]):
            # Check if the current character exists in all other strings
            for string in strs[1:]:
                # If the index is greater than or equal to the length of the current string
                # or the character does not match, return the prefix up to the current index
                if index >= len(string) or char != string[index]:
                    return strs[0][:index]
        
        # If all strings have the same characters, return the first string as the common prefix
        return strs[0]

solution = Solution()

print (solution.longestCommonPrefix(["flower","flow","flight"]))
# Output: "fl"

print (solution.longestCommonPrefix(["dog","racecar","car"]))
# Output: ""
