class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def bfs(coins, ptr, goal, dp):
            if goal == 0:
                return 0
            if ptr == len(coins) or goal < 0:
                return float("inf")

            if (ptr, goal) not in dp:
                dp[(ptr, goal)] = min(
                        bfs(coins, ptr+1, goal, dp),
                        1 + bfs(coins, ptr, goal-coins[ptr], dp)
                    )
            return dp[(ptr, goal)]
        dp = dict()
        ans = bfs(coins, 0, amount, dp)
        return -1 if ans == float("inf") else ans