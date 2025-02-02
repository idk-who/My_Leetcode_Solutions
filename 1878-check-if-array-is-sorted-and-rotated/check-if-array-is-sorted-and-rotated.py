class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        ptr = 1

        while ptr < n and nums[ptr] >= nums[ptr-1]:
            ptr += 1
        if ptr == n:
            return True

        ptr += 1
        while ptr < n and nums[ptr] >= nums[ptr-1]:
            ptr += 1
        
        if ptr < n or nums[0] < nums[-1]:
            return False

        return True