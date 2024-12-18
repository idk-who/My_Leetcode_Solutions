class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        stack = []
        for i in range(len(prices)-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            if stack:
                ans.append(prices[i]-stack[-1])
            else:
                ans.append(prices[i])

            stack.append(prices[i])
        
        return ans[::-1]