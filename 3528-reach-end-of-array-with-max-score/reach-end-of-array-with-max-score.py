class Solution:
    def findMaximumScore(self, arr: List[int]) -> int:
        return sum(accumulate(arr[:-1], max))
