# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to their integer values.
        T = {
             "I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000
            }
        
        # Initialize a variable to store the final integer result.
        result = 0
        
        # Iterate through the Roman numeral string.
        for i in range(len(s)):
            # Check if the current numeral is smaller than the next numeral (subtractive notation).
            if i < len(s) - 1 and T[s[i]] < T[s[i + 1]]:
                # If so, subtract its value from the result.
                result -= T[s[i]]
            else:
                # Otherwise, add its value to the result.
                result += T[s[i]]
        
        # Return the computed integer result.
        return result

# Test the 'romanToInt' function with a sample test case.
if __name__ == "__main__":
    # Create an instance of the 'Solution' class.
    solution = Solution()
    
    # Test case: Convert the Roman numeral "III" to an integer.
    # Expected output: 3 (I + I + I = 1 + 1 + 1 = 3).
    result1 = solution.romanToInt("III")
    print("Test Case 1:", result1)  # Output: 3
    
    # Test case: Convert the Roman numeral "LVIII" to an integer.
    # Expected output: 58 (L + V + III = 50 + 5 + 3 = 58).
    result2 = solution.romanToInt("LVIII")
    print("Test Case 2:", result2)  # Output: 58
    
    # Test case: Convert the Roman numeral "MCMXCIV" to an integer.
    # Expected output: 1994 (M + CM + XC + IV = 1000 + 900 + 90 + 4 = 1994).
    result3 = solution.romanToInt("MCMXCIV")
    print("Test Case 3:", result3)  # Output: 1994
