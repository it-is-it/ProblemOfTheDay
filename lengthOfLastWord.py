# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.\

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words) > 0:
            return len(words[-1])
        else:
            return 0
        
solution = Solution()
s1 = "Hello World"
print(solution.lengthOfLastWord(s1))
# Output: 5

s2 = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s2))
# Output: 4

s3 = "luffy is still joyboy"
print(solution.lengthOfLastWord(s3))
# Output: 6