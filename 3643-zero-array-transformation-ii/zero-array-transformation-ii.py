class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        diff = [0]*(n+1)
        k = 0
        su = 0
        for i in range(n):
            while su + diff[i] < nums[i]:
                if k >= len(queries):
                    return -1
                l, r, v = queries[k]
                if r >= i:
                    diff[max(i, l)] += v
                    diff[r+1] -= v
                k += 1
            
            su += diff[i]
        
        return k
