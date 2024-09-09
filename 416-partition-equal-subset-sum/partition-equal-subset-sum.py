class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su&1:
            return False
        tar = su//2
        dp = dict()
        def rec(nums, ptr, tar, dp):
            if tar == 0:
                return True
            if tar < 0 or ptr == len(nums):
                return False
            if (ptr, tar) in dp:
                return dp[(ptr, tar)]
            
            val = (
                rec(nums, ptr+1, tar, dp) or
                rec(nums, ptr+1, tar-nums[ptr], dp)
            )
            dp[(ptr, tar)] = val

            return val
        
        return rec(nums, 0, tar, dp)
