class Solution:
    def isSorted(self, arr) -> bool:
        n = len(arr)
        for i in range(0,n-1):
            if arr[i] > arr[i+1]:
                return False
        return True
arr = [90, 80, 100, 70, 40, 30]
sol = Solution()
sol.isSorted(arr)