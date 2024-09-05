class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        '''
        m = cMean
        S = cSum
        (S + Diff)/(n+m) == mean
        Diff = (mean*(n+m))-S
        '''
        m = len(rolls)
        S = sum(rolls)
        diff = (mean*(n+m))-S
        if (diff / n) < 1 or (diff / n) > 6: return []

        quo = diff//n
        rem = diff%n
        ans = [quo] * n
        ans = [quo + (i < rem) for i in range(n)]
        return ans
        
        