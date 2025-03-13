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
        
        ind = bisect.bisect_left(
            list(range(len(queries))), 
            1, 
            key = lambda x: is_zero(x)
        )
        if ind+1 <= len(queries):
            return ind+1
        return -1
        
