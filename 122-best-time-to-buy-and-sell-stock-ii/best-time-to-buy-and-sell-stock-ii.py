class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2 pointer approach

        Algo:

        i = buy date
        j = sell date

        i, j = 0
        iterate till j<len(array)
            profit = j-i
            if profit<0:
                j++
            else: 
                total_profit+=profit
                j++
            i=j
        
        """

        i = 0 
        j = 0
        total_profit = 0
        for j in range(len(prices)):
            profit = prices[j]-prices[i]
            
            if profit>0:
                total_profit+=profit
            i=j
        
        return total_profit