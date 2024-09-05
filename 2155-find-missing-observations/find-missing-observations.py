class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        '''
        m = len(rolls)
        S = sum(rolls)
        (S + Diff)/(n+m) == mean
        Diff = (mean*(n+m))-S
        '''
        diff = (mean*(n+len(rolls)))-sum(rolls)
        if diff < n or diff > 6*n: return []

        quo = diff//n
        rem = diff%n
        ans = [quo + (i < rem) for i in range(n)]
        return ans
    
        