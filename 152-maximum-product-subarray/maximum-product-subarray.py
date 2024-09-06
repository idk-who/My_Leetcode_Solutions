class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        pre = 1
        suf = 1
        for i in range(n):
            if pre == 0: pre = 1
            if suf == 0: suf = 1
            pre *= nums[i]
            suf *= nums[n - 1 - i]
            ans = max(ans, pre, suf)

        return ans

