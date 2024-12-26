class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = dict()
        def rec(ptr, su):
            if ptr == n:
                return su == target
            
            if (ptr, su) in dp:
                return dp[(ptr, su)]
            
            poss = (
                rec(ptr+1, su+nums[ptr]) + 
                rec(ptr+1, su-nums[ptr])
            )
            dp[(ptr, su)] = poss

            return poss
        
        return rec(0, 0)