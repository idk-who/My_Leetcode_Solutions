class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        dp = dict()
        def recurse(nums, ptr, s):
            if s == 0:
                return True
            if ptr == len(nums):
                return False
            if (ptr, s) not in dp:
                dp[(ptr, s)] = recurse(nums, ptr+1, s) or recurse(nums, ptr+1, s-nums[ptr])
            return dp[(ptr, s)]

        if su & 1:
            return False
        else:
            return recurse(nums, 0, su//2)
