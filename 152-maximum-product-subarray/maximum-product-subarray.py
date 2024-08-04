class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = nums[0]
        imin = nums[0]
        r = nums[0]

        s1 = False
        for i in nums:
            if not s1:
                s1 = True
                continue
            candidates = (i, imax*i, imin*i)

            imax = max(candidates)
            imin = min(candidates)

            r = max(r, imax)

        return r


            
