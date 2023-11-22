class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_indexes = [idx for idx, value in enumerate(nums[:-1]) if value == 0]
        
        for zero_ind in zero_indexes:
            for i in range(zero_ind):
                zero_ind-=1
                if nums[zero_ind]>i+1:
                    break   
            else:
                return False
                
        return True
