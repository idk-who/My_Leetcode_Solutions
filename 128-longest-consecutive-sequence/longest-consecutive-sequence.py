class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)

        nums.sort()
        ans = 1
        lmax = 1 # local max
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]: 
                continue
            if nums[i-1]+1 == nums[i]:
                lmax += 1
            else:
                lmax = 1
            ans = max(ans, lmax)
        
        return ans