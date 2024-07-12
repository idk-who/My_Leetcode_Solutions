class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict() # ptr, li
        def rec(prices, ptr, li, bought):
            if ptr >= len(prices) or li == 0:
                return 0

            nonlocal dp
            if (ptr, li, bought) not in dp:
                dp[(ptr, li, bought)] = rec(prices, ptr+1, li, bought)
                if bought:
                    dp[(ptr, li, bought)] = max(
                        dp[(ptr, li,bought)],
                        prices[ptr] + rec(prices, ptr+1, li-1, False),
                    )
                else:
                    dp[(ptr, li, bought)] = max(
                        dp[(ptr, li, bought)],
                        - prices[ptr] + rec(prices, ptr+1, li, True),
                    )

            
            return dp[(ptr, li, bought)]
        # rec(prices, 0, 0, 0, 2)
        # print(dp)
        return rec(prices, 0, 2, False)

