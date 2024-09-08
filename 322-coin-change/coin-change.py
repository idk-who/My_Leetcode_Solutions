class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')]*(amount+1) for i in range(len(coins))]
        dp[0][0] = 0
        for i in range(len(coins)):
            dp[i][0] = 0

        for i in range(len(coins)):
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j]
                if coins[i] <= j:
                    dp[i][j] = min(
                        dp[i][j],
                        1 + dp[i-1][j-coins[i]],
                        1 + dp[i][j-coins[i]]
                    )
                    
        
        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1


