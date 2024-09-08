class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        coins.sort()
        for j in range(1, amount+1):
            for i in range(len(coins)):
                if coins[i] <= j:
                    dp[j] = min(dp[j], 1 + dp[j-coins[i]])
                else:
                    break
        
        return dp[-1] if dp[-1] != float("inf") else -1
