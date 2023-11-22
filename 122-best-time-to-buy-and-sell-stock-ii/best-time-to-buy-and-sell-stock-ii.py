class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 0
        total_profit = 0
        for j in range(len(prices)):
            profit = prices[j]-prices[i]
            
            if profit>0:
                total_profit+=prices[j]-prices[i]
            i=j
        
        return total_profit