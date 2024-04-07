class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        m = n + 1 # min len of subarray
        l = 0     # low 
        s = 0     # sum variable (collector)

        for h in range(n):
            s += nums[h]
            while s >= target:
                if h-l+1<m: m = h-l+1
                s -= nums[l]
                l += 1
        
        if m == len(nums) + 1: return 0 
        else: return m
