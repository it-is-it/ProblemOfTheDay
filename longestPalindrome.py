#409. Longest Palindrome
#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
 
# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1

class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency_map = {}
        for c in s:
            frequency_map[c] = frequency_map.get(c, 0) + 1
        res = 0
        has_odd_frequency = False
        for freq in frequency_map.values():
            if (freq % 2) == 0:
                res += freq
            else:
                res += freq - 1
                has_odd_frequency = True
        if has_odd_frequency:
            return res + 1
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))