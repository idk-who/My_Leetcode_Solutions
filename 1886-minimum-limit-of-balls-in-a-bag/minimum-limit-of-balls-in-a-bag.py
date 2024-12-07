class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def is_poss(penalty):
            count = 0
            for i in nums:
                if i > penalty:
                    count += (i-1)//penalty
            return count <= maxOperations

        l = 1
        r = max(nums)

        while l < r:
            m = (l+r)//2
            if is_poss(m):
                r = m
            else:
                l = m + 1
        
        return l