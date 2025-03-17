class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return reduce(lambda x, y: x^(1<<y), [0]+nums) == 0