# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a memoization dictionary to store calculated results
        memo = {}

        # Helper function for recursive calls with memoization
        def climb(n):
            # If n is 1 or 2, there is only one way to climb (returning 1 or 2)
            if n == 1 or n == 2:
                return n
            
            # Check if the result for n is already in memo
            if n in memo:
                return memo[n]

            # Calculate and store the result in memo
            memo[n] = climb(n - 1) + climb(n - 2)

            return memo[n]

        # Call the helper function with the input value
        return climb(n)

# Example usage:
solution = Solution()
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(4))  # Output: 5
