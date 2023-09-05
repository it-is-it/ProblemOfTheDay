# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
# Example 2:

# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
 
from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = salary[0]  # Initialize max_salary with the first salary in the list
        min_salary = salary[0]  # Initialize min_salary with the first salary in the list
        total_salary = 0       # Initialize total_salary to 0
        
        for s in salary:
            if s > max_salary:
                max_salary = s  # Update max_salary if a larger salary is found
            if s < min_salary:
                min_salary = s  # Update min_salary if a smaller salary is found
            total_salary += s   # Accumulate salaries to calculate the sum
        
        # Calculate the average after the loop
        average_salary = (total_salary - min_salary - max_salary) / (len(salary) - 2)
        
        return average_salary

def main():
    solution = Solution()
    
    # Test case 1: Sample test case
    salary1 = [4000, 3000, 1000, 2000]
    result1 = solution.average(salary1)
    print(f"Average Salary (Test Case 1): {result1:.2f}")
    
    # Test case 2: Test with negative salaries
    salary2 = [-100, -200, -300, -400, -500]
    result2 = solution.average(salary2)
    print(f"Average Salary (Test Case 2): {result2:.2f}")
    
    # Test case 3: Test with salaries where minimum and maximum are the same
    salary3 = [5000, 5000, 5000, 5000]
    result3 = solution.average(salary3)
    print(f"Average Salary (Test Case 3): {result3:.2f}")

if __name__ == "__main__":
    main()
