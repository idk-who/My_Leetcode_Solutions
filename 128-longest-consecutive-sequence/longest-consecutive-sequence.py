class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        
        ans = 0

        for i in nums:
            if i-1 not in st:
                lmax = 1 # local max
                while i+1 in st:
                    lmax += 1
                    i += 1
                ans = max(ans, lmax)
        
        return ans