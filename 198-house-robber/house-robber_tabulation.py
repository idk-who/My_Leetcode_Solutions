class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        n = len(nums)
        dp = [0]*(n+1)
        dp[n] = 0
        dp[n-1] = nums[-1]
        dp[n-2] = max(nums[-2], nums[-1]) 

        for i in range(n-3, -1, -1):
            dp[i] = max(nums[i]+dp[i+2], nums[i+1]+dp[i+3]) 

        return dp[0]
