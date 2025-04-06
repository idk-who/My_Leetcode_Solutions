class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        dp = {}
        def rec(prev, ptr):
            if ptr == n:
                return []
            
            if prev in dp:
                return dp[prev]
            
            if prev == -1 or nums[ptr]%prev == 0:
                ma = max(
                    rec(prev, ptr+1),
                    [nums[ptr]] + rec(nums[ptr], ptr + 1),
                    key = len
                )
            else:
                ma = rec(prev, ptr+1)
            
            dp[prev] = ma
            return ma

        return rec(-1, 0)