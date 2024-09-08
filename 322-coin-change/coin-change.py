class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1]*(amount+1)
        memo[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                sub = i - c

                if sub < 0:
                    continue
                
                if memo[sub] + 1 < memo[i]:
                    memo[i] = memo[sub] + 1
        
        if memo[amount] == amount+1:
            return -1
        
        return memo[amount]