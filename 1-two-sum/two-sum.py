class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for ind, ele in enumerate(nums):
            if target-ele in d:
                return d[target-ele], ind
            d[ele] = ind
        
        return -1, -1
