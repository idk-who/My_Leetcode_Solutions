class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su&1:
            return False
        tar = su//2

        n = len(nums)
        dp = [False]*(tar+1)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(tar, -1, -1):
                if j >= nums[i-1]:
                    dp[j] = (
                        dp[j] or
                        dp[j-nums[i-1]]
                    )
        
        return dp[-1]
