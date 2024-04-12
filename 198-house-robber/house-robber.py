class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        n = len(nums)

        first = 0
        second = nums[-1]
        third = max(nums[-2], nums[-1])

        for i in range(n-3, -1, -1):
            third, second, first = max(nums[i]+second, nums[i+1]+first), third, second

        return third
