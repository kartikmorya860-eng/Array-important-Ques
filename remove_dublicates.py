class Solution:

    def removeDuplicates(self, nums):
        i = 0
        n = len(nums)
        ans = [nums[0]]
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                ans.append(nums[j])
                nums[i] = nums[j]
        return ans
            
        