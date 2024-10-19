class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ma = 0
        for i in nums: ma |= i

        def rec(ptr, temp_or):
            if ptr == len(nums):
                if temp_or == ma:
                    return 1
                return 0
            return (
                rec(ptr+1, temp_or) +
                rec(ptr+1, temp_or|nums[ptr])
            )
        
        return rec(0, 0)



