class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def rec(nums, target, ptr, dp):
            if ptr == len(nums):
                return target == 0

            if (ptr, target) not in dp:
                dp[(ptr, target)] = (
                    rec(nums, target-nums[ptr], ptr+1, dp) +
                    rec(nums, target+nums[ptr], ptr+1, dp)
                )
            return dp[(ptr, target)]
        
        return rec(nums, target, 0, dict())