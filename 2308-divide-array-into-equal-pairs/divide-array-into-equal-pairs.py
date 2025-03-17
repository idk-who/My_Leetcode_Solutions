class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = 0
        for i in nums:
            s ^= (1<<i)
        return s == 0