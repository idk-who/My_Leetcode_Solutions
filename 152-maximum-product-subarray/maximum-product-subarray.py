class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = nums[0]
        mi = nums[0]
        ma = nums[0]
        for i in nums[1:]:
            candidates = (i, mi*i, ma*i)
            mi = min(candidates)
            ma = max(candidates)
            ans = max(ans, ma)

        return ans

