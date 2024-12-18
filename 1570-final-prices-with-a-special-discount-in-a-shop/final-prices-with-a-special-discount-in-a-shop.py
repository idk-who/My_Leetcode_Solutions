class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []

        for i in range(len(prices)):
            sp = prices[i]
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= sp:
                    discount = prices[j]
                    break
            ans.append(sp-discount)
        
        return ans