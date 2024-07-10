class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)

        if su & 1: return False
        k = su // 2
        dp = 1
        for num in nums:
            dp |= dp << num
        return dp & (1<<k)
