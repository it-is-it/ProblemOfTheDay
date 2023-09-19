# 1624. Largest Substring Between Two Equal Characters

# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
 


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_distance = -1  # Initialize the maximum distance to -1

        # Loop through each character in the string
        for i in range(len(s)):
            # Inner loop to compare with characters to the right of the current character
            for j in range(len(s) - 1, i, -1):
                if s[i] == s[j]:
                    # Calculate the distance between equal characters
                    distance = j - i - 1
                    # Update max_distance if the current distance is greater
                    max_distance = max(max_distance, distance)

        return max_distance

# Test cases
solution = Solution()

# Test case 1: "aa" => The maximum distance is between 'a' at index 0 and 'a' at index 1 (distance = 0)
print(solution.maxLengthBetweenEqualCharacters("aa"))  # Output: 0

# Test case 2: "abca" => The maximum distance is between 'a' at index 0 and 'a' at index 3 (distance = 2)
print(solution.maxLengthBetweenEqualCharacters("abca"))  # Output: 2

# Test case 3: "cbzxy" => No equal characters, so the result is -1
print(solution.maxLengthBetweenEqualCharacters("cbzxy"))  # Output: -1


