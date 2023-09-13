# 2409. Count Days Spent Together

# Alice and Bob are traveling to Rome for separate business meetings.

# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

# Return the total number of days that Alice and Bob are in Rome together.

# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

 

# Example 1:

# Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
# Example 2:

# Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# Output: 0
# Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

from datetime import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_day_format ="%m-%d"
        arriveAlice_date = datetime.strptime(arriveAlice, month_day_format)
        leaveAlice_date = datetime.strptime(leaveAlice, month_day_format)
        arriveBob_date = datetime.strptime(arriveBob, month_day_format)
        leaveBob_date = datetime.strptime(leaveBob, month_day_format)


        start_date = max(arriveAlice_date,arriveBob_date)
        end_date = min(leaveAlice_date,leaveBob_date)

        overlap_days = (end_date -start_date).days +1
        return max(0, overlap_days)
    
if __name__ =="__main__":
    solution = Solution()
    
    example1 = solution.countDaysTogether("08-15","08-18","08-16","08-19")
    print(example1) # Output: 3
    example2 = solution.countDaysTogether("10-01","10-31","11-01","12-31")
    print(example2) # Output: 0
