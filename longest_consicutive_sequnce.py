class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        last_smaller = float("-inf")
        count = 0
        longest = 0
        nums.sort()
        n = len(nums)
        for i in range(0,n):
            num = nums[i]

            if num  == last_smaller:
                continue

            if num-1 == last_smaller:
                count +=1
                last_smaller = num
                
            else:
                count = 1
                last_smaller = num
            longest = max(longest,count)
        return longest
        