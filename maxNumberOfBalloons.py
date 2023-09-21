# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 







class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = 0
        T = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0,
        }
        
        for char in text:
            if char in T:
                T[char] += 1
        
        T['l'] //= 2 
        T['o'] //= 2  
        
        while all(T[key] > 0 for key in T.keys()):
            ans += 1
            for key in T.keys():
                T[key] -= 1
        
        return ans


# Test the Solution class
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Should return 1
    input_str1 = "nlaobllnoa"
    result1 = solution.maxNumberOfBalloons(input_str1)
    print(f"Test case 1: {result1}")
    
    # Test case 2: Should return 2
    input_str2 = "balloonballoon"
    result2 = solution.maxNumberOfBalloons(input_str2)
    print(f"Test case 2: {result2}")
    
    # Test case 3: Should return 0
    input_str3 = "ban"
    result3 = solution.maxNumberOfBalloons(input_str3)
    print(f"Test case 3: {result3}")
    
    # Test case 4: Should return 0
    input_str4 = "loonbalx"
    result4 = solution.maxNumberOfBalloons(input_str4)
    print(f"Test case 4: {result4}")
