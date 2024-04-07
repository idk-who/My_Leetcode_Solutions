class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)


        m = len(nums) + 1 # min len of subarray
        l = 0   # low 
        h = 0   # high 
        s = 0   # sum variable (collector)

        while h<n:
            s += nums[h]
            h += 1

            while s >= target:
                if h-l<m: m = h-l
                s -= nums[l]
                l += 1
        
        if m == len(nums) + 1: return 0 
        else: return m