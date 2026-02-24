class Solution:
    def largest(self, arr):
        largest_e = arr[0]
        for i in range(0,len(arr)):
            largest_e = max(largest_e,arr[i])
        return largest_e
