class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid =len(nums)//2
        L = nums[:mid]
        R = nums[mid:]
        L= self.sortArray(L)
        R= self.sortArray(R)
 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
        return nums

solution = Solution()
nums = [5, 2, 9, 3, 6]
sorted_nums = solution.sortArray(nums)
print(sorted_nums)