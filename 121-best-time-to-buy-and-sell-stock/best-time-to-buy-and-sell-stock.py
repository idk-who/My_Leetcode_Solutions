class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        i = 0
        for j in range(len(prices)):
            profit = prices[j]-prices[i]
            if profit < 0:
                i=j
            elif profit > max:
                max = profit
        
        return max
