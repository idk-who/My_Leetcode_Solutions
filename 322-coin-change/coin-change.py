class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                if coins[i] <= j:
                    dp[j] = min(dp[j], 1 + dp[j-coins[i]])
        
        return dp[-1] if dp[-1] != float("inf") else -1
