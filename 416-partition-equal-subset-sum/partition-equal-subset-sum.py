class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)

        if su & 1:
            return False
        else:
            k = su // 2
            n = len(nums)
            dp = [[False]*(k+1) for i in range(n)]
            dp[0][0] = True
            if nums[0] <= k:
                dp[0][nums[0]] =  True
            for i in range(1, n):
                dp[i][0] = True
                for t in range(1, k+1):
                    dp[i][t] = dp[i-1][t] or (dp[i-1][t-nums[i]] if nums[i] <= t else False)
            return dp[-1][-1]
