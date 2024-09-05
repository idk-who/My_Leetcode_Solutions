class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        '''
        m = cMean
        S = cSum
        (S + Diff)/(n+m) == mean
        Diff = (mean*(n+m))-S
        '''
        diff = (mean*(n+len(rolls)))-sum(rolls)
        if diff < n or diff > 6*n: return []

        quo = diff//n
        rem = diff%n
        ans = [quo] * n
        for i in range(rem): ans[i] += 1
        return ans
    
        