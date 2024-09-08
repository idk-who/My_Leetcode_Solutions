class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1]*(amount+1) for i in range(len(coins))]

        def rec(coins, amount, ptr, dp):
            if amount == 0:
                return 0
            if amount < 0 or ptr == len(coins):
                return float("inf")
            
            if dp[ptr][amount] != -1:
                return dp[ptr][amount]
            
            mi = min(
                rec(coins, amount, ptr+1, dp),
                1 + rec(coins, amount-coins[ptr], ptr, dp)
            )
            dp[ptr][amount] = mi

            return mi

        ans = rec(coins, amount, 0, dp)
        return ans if ans != float('inf') else -1




