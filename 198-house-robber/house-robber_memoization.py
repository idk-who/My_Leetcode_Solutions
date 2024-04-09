class Solution:
    def rob(self, nums: List[int]) -> int:

        self.dp = [None]*len(nums)
        return self.helper(nums, 0)
        
    def helper(self, nums, start):
        if start > len(nums) - 1:
            return 0 
        elif start == len(nums) - 1:
            return nums[start]
        if self.dp[start] is None:
            self.dp[start] = max(
                nums[start] + self.helper(nums, start+2),
                nums[start+1] + self.helper(nums, start+3)
            )
        return self.dp[start]
