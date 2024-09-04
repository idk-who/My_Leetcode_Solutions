class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))
        nums.sort(key = lambda x: x[1])

        p1 = 0 
        p2 = len(nums) - 1

        while p1 < p2:
            if nums[p1][1] + nums[p2][1] == target:
                return nums[p1][0], nums[p2][0]
            elif nums[p1][1] + nums[p2][1] < target:
                p1 += 1
            else:
                p2 -= 1
                
        return -1, -1