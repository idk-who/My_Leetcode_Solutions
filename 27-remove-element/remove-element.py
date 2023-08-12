class Solution:
    def removeElement(self, nums, val: int) -> int:

        ptr = 0 
        incr = 0

        while ptr+incr<len(nums):
            print(ptr, ptr+incr, "||", nums)
            while ptr+incr<len(nums) and nums[ptr+incr] == val:
                incr += 1
            if ptr+incr>=len(nums): 
                break
            nums[ptr] = nums[ptr+incr]
            ptr += 1
        
        return ptr