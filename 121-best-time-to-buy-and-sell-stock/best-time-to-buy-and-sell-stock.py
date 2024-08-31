class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float("inf")
        ans = 0

        for i in prices:
            if i < mi:
                mi = i
            elif i - mi > ans:
                ans = i - mi

        return ans