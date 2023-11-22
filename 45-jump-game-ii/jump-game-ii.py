class Solution:
    def jump(self, nums: List[int]) -> bool:
        reach_old = 0
        reach = 0
        ptr = 0
        moves = 0

        while ptr<len(nums)-1:
            reach = max(reach, ptr+nums[ptr])
            if reach>=len(nums)-1:
                moves+=1
                return moves
            if ptr >= reach_old:
                moves+=1
                reach_old = reach
            ptr+=1
            
        return moves
