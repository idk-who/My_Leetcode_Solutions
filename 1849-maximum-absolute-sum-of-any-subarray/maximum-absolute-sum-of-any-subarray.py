class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ma = 0
        su = 0
        for i in nums:
            su += i
            if su < 0:
                su = 0
            ma = max(ma, su)
        
        mi = 0
        su = 0
        for i in nums:
            su += i
            if su > 0:
                su = 0
            mi = min(mi, su) 
        
        return max(ma, abs(mi))