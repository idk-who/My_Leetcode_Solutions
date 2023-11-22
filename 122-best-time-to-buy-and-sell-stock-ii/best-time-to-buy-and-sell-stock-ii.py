class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        total_profit = 0
        for j in range(1,len(prices)):
            profit = prices[j]-prices[j-1]
            
            if profit>0:
                total_profit+=profit
        
        return total_profit