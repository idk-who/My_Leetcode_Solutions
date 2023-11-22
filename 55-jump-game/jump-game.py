class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = nums[0]
        ptr = 0
        while ptr<len(nums) and ptr<=reach:
            reach = max(reach, ptr+nums[ptr])
            if reach>=len(nums)-1:
                return True
            ptr+=1
        return False
