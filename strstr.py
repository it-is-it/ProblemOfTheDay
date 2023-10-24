# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.\


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         for index , char in enumerate(haystack):
#             if char in needle:
#                 print(f"Character '{char}' is present in both strings.")
#             else:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if the needle is an empty string
        if not needle:
            return 0
        
        # Iterate through the haystack using sliding window approach
        for index in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack matches the needle
            if haystack[index:index + len(needle)] == needle:
                # If it matches, return the index of the first character of the needle in the haystack
                return index
        
        # If the needle is not found in the haystack, return -1
        return -1

# Example usage
solution = Solution()
# Test cases
print(solution.strStr("sadbutsad", "sad"))  # Output: 0 (needle "sad" starts at index 0)
print(solution.strStr("leetcode", "leeto"))  # Output: -1 (needle "leeto" is not found in haystack)
