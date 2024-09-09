class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su&1:
            return False
        
        tar = su//2
        dp = 1

        for i in nums:
            dp |= (dp<<i)
        
        return dp & (1<<tar)
