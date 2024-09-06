class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")

        pre = 1
        for i in nums:
            if pre == 0: pre = 1
            pre *= i
            ans = max(ans, pre)

        suf = 1
        for i in reversed(nums):
            if suf == 0: suf = 1
            suf *= i
            ans = max(ans, suf)
        
        return ans

        