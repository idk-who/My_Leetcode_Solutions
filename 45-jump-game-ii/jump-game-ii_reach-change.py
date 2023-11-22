class Solution:
    def jump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return 0

        reach_old = nums[0]
        reach = reach_old
        ptr = 0
        moves = 1

        while ptr<=len(nums)-2:
            reach = max(reach, ptr+nums[ptr])
            if reach!=reach_old and ptr >= reach_old:
                moves+=1
                reach_old = reach
            ptr+=1
        
        return moves
