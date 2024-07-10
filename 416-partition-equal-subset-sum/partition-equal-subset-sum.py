class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)

        if su & 1:
            return False
        else:
            k = su // 2
            n = len(nums)
            dp = [False]*(k+1)
            dp[0] = True
            if nums[0] <= k:
                dp[nums[0]] =  True
            new_dp = [False]*(k+1)

            for i in range(1, n):
                for t in range(k+1):
                    new_dp[t] = dp[t] or (dp[t-nums[i]] if nums[i] <= t else False)
                dp[:] = new_dp
            return dp[-1]
