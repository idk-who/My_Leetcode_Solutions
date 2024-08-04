class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = nums[0]
        imin = nums[0]
        r = nums[0]

        for i in nums[1:]:
            candidates = (i, imax*i, imin*i)

            imax = max(candidates)
            imin = min(candidates)

            r = max(r, imax)

        return r


            
