class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def is_zero(k):
            pre = [0]*n
            for i in range(k+1):
                l, r, v = queries[i]
                pre[l] += v
                if r+1 < n:
                    pre[r+1] -= v
            su = 0
            for i in range(n):
                su += pre[i]
                if su < nums[i]:
                    return False
            return True

        if sum(nums) == 0: return 0
        
        l, r = 0, len(queries) - 1

        while l <= r:
            m = (l+r)//2
            if is_zero(m):
                r = m - 1
            else:
                l = m + 1
        
        if l+1 <= len(queries):
            return l+1
        return -1
        
