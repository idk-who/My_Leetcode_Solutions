class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]

        ans = 0
        for i in range(len(nums)//2):
            ans += nums[len(nums)-i-1] - nums[i]
        return ans
