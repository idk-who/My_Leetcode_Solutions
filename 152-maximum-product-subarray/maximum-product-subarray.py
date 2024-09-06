class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = nums[0]
        mi = nums[0]
        ma = nums[0]
        for i in range(1, n):
            new_mi = min(nums[i], mi*nums[i], ma*nums[i])
            ma = max(nums[i], mi*nums[i], ma*nums[i])
            mi = new_mi
            ans = max(ans, ma)

        return ans

