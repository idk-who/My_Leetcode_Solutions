class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        su = 0
        tn = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            if su + i > maxSum:
                return tn
            su += i
            tn += 1
        return tn