class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su&1:
            return False
        tar = su//2
        n = len(nums)
        dp = [[False]*(tar+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, tar+1):
                if j >= nums[i-1]:
                    dp[i][j] = (
                        dp[i-1][j] or
                        dp[i-1][j-nums[i-1]]
                    )
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
