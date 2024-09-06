class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = nums[0]
        mi = nums[0]
        ma = nums[0]
        for i in range(1, n):
            candidates = (nums[i], mi*nums[i], ma*nums[i])
            mi = min(candidates)
            ma = max(candidates)
            ans = max(ans, ma)

        return ans

