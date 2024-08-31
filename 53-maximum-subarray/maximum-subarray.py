class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        ma = 0
        for i in nums:
            ma += i

            ans = max(ans, ma)

            if ma < 0: ma = 0
        
        return ans