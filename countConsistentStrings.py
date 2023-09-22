# 1684. Count the Number of Consistent Strings

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

# Example 1:
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# Example 2:
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.

# Example 3:
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            is_consistent = True
            for char in word:
                if char not in allowed:
                    is_consistent = False
                    break
            if is_consistent:
                ans += 1
        return ans

# Test the Solution class
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Should return 2
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    result1 = solution.countConsistentStrings(allowed,words)
    print(f"Test case 1: {result1}")
    
    # Test case 2: Should return 7
    allowed = "abc"
    words = ["a","b","c","ab","ac","bc","abc"]
    result1 = solution.countConsistentStrings(allowed,words)
    print(f"Test case 1: {result1}")
    
    # Test case 3: Should return 4
    allowed = "cad"
    words = ["cc","acd","b","ba","bac","bad","ac","d"]
    result1 = solution.countConsistentStrings(allowed,words)
    print(f"Test case 1: {result1}")