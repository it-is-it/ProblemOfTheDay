# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 
# Import the math module for math.floor
import math

# Define the countBits function, which calculates the number of 1's in the binary representation of numbers from 0 to n.
def countBits(n):
    # Initialize a list to store the results, with n+1 zeros (since we want to calculate for numbers from 0 to n)
    ans = [0] * (n + 1)

    # Iterate through numbers from 1 to n
    for i in range(1, n + 1):
        # Calculate the number of 1's in the binary representation of i
        # ans[i] = ans[i >> 1] + (i & 1)

        # Shift i one position to the right (effectively dividing by 2) and add the least significant bit of i
        ans[i] = ans[i >> 1] + (i & 1)

    # Return the list containing the number of 1's for each number from 0 to n
    return ans

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Set an example value for n (you can change this to any integer)
    n = 5

    # Call the countBits function with n as input and store the result
    result = countBits(n)

    # Print the result, which is a list containing the number of 1's in binary representation from 0 to n
    print(result)  # Output: [0, 1, 1, 2, 1, 2]
