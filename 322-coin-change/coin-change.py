class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')]*(amount+1) for i in range(len(coins)+1)]
        dp[0][0] = 0
        for i in range(len(coins)+1):
            dp[i][0] = 0

        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(
                        dp[i-1][j],
                        1 + dp[i-1][j-coins[i-1]],
                        1 + dp[i][j-coins[i-1]]
                    )
                else:
                    dp[i][j] = dp[i-1][j]
        # for i in dp:
        #     print(i)
        
        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1


