class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        s = 0
        e = len(nums)-1
        while s<e:
            if -nums[s] == nums[e]:
                return nums[e]
            elif -nums[s] < nums[e]:
                e -= 1
            else:
                s += 1
        
        return -1
