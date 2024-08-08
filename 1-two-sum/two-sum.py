class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = list(enumerate(nums))
        temp.sort(key = lambda x: x[1])
        nums.sort()

        p1 = 0
        p2 = len(nums)-1

        while p1 < p2:
            if nums[p1] + nums[p2] == target:
                return [temp[p1][0], temp[p2][0]]
            elif nums[p1] + nums[p2] > target:
                p2 -= 1
            else:
                p1 += 1
        

        