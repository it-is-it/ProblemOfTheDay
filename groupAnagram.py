# 49. Group Anagrams
# Given an array of strings strs, group the  anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups of anagrams
        anagrams = defaultdict(list)
        
        for word in strs:
            # Create a sorted version of the string as the key
            sorted_word = ''.join(sorted(word))
            # Group words by the sorted version
            anagrams[sorted_word].append(word)
        
        # Return grouped anagrams as a list of lists
        return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs))

strs2 = [""]
solution = Solution()
print(solution.groupAnagrams(strs2))

str3 = ["a"]
solution = Solution()
print(solution.groupAnagrams(str3))
