class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ma = 0
        for i in nums: ma |= i
        ans = [0]

        def rec(ptr, temp_or):
            if ptr == len(nums):
                if temp_or == ma:
                    ans[0] += 1
                return 
            rec(ptr+1, temp_or)
            rec(ptr+1, temp_or|nums[ptr])
        
        rec(0, 0)
        return ans[0]