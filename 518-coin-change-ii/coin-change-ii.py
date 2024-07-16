class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins))]

        def rec(coins, ptr, target, dp):
            if target == 0:
                return 1
            if ptr == len(coins) or target < 0:
                return 0
            
            if dp[ptr][target] == -1:
                dp[ptr][target] = (
                    rec(coins, ptr + 1, target, dp) + 
                    rec(coins, ptr, target-coins[ptr], dp)
                )
            
            return dp[ptr][target]
        
        return rec(coins, 0, amount, dp)