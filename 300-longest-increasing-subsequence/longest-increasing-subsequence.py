class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1]*len(nums) for i in range(len(nums))]

        def lis(nums, ptr, prev_ind, dp):
            if ptr == len(nums):
                return 0

            if dp[ptr][prev_ind] != -1:
                return dp[ptr][prev_ind]
            
            ma = lis(nums, ptr + 1, prev_ind, dp)
            if prev_ind == -1 or nums[ptr] > nums[prev_ind]:
                ma = max(
                    ma, 1 + lis(nums, ptr+1, ptr, dp)
                )     
            dp[ptr][prev_ind] = ma
            return ma
        
        return lis(nums, 0, -1, dp)