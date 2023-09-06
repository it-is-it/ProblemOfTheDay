# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums, target):
        # Initialize an empty dictionary to store numbers and their indices.
        numMap = {}
        
        # Get the length of the 'nums' list.
        n = len(nums)
        
        # Iterate through the 'nums' list using a loop.
        for i in range(n):
            # Calculate the complement (the value needed to reach the 'target').
            complement = target - nums[i]
            
            # Check if the complement is already in the 'numMap'.
            if complement in numMap:
                # If found, return a list with the indices of the two numbers that sum to the 'target'.
                return [numMap[complement], i]
            
            # If the complement is not in 'numMap', store the current number and its index in 'numMap'.
            numMap[nums[i]] = i
        
        # If no solution is found, return an empty list.
        return []

# Test the 'twoSum' function with a sample test case.
if __name__ == "__main__":
    # Create an instance of the 'Solution' class.
    solution = Solution()
    
    # Test case 1: Find two numbers that sum to 9 in the list [2, 7, 11, 15].
    # Expected output: The indices of the numbers 2 and 7, which are [0, 1].
    result1 = solution.twoSum([2, 7, 11, 15], 9)
    print("Test Case 1:", result1)  # Output: [0, 1]
    
    # Test case 2: Find two numbers that sum to 6 in the list [3, 2, 4].
    # Expected output: The indices of the numbers 2 and 4, which are [1, 2].
    result2 = solution.twoSum([3, 2, 4], 6)
    print("Test Case 2:", result2)  # Output: [1, 2]
    
    # Test case 3: Find two numbers that sum to 6 in the list [3, 3].
    # Expected output: The indices of the numbers 3 and 3, which are [0, 1].
    result3 = solution.twoSum([3, 3], 6)
    print("Test Case 3:", result3)  # Output: [0, 1]
