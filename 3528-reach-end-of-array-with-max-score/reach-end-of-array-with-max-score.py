class Solution:
    def findMaximumScore(self, arr: List[int]) -> int:
        ans = 0 
        ma = 0
        for i in arr[:-1]:
            if i > ma: ma = i
            ans += ma
        return ans
