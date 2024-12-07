class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def is_poss(penalty):
            mop = maxOperations
            for i in nums:
                if i > penalty:
                    mop -= ((i//penalty) + ((i%penalty) > 0)) - 1
                if mop < 0:
                    return False
            return True

        l = 1
        r = max(nums)

        while l < r:
            m = (l+r)//2
            if is_poss(m):
                r = m
            else:
                l = m + 1
        
        return l