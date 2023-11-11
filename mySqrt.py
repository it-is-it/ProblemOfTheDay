# 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        # Check if x is 0, in which case the square root is also 0
        if x == 0:
            return 0
        
        # Initialize the search space using binary search
        first, last = 1, x
        
        # Perform binary search until the search space is exhausted
        while first <= last:
            # Calculate the midpoint
            mid = first + (last - first) // 2
            
            # Check if the square of the midpoint is equal to x
            if mid == x // mid:
                return mid
            # If the square of the midpoint is greater than x, narrow the search space to the left
            elif mid > x // mid:
                last = mid - 1
            # If the square of the midpoint is less than x, narrow the search space to the right
            else:
                first = mid + 1
        
        # The loop ends when the search space is exhausted, return the last valid result
        return first - 1

solution = Solution()
print(solution.mySqrt(4))
print(solution.mySqrt(8))