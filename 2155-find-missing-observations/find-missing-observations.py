class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        '''
        m = len(rolls)
        S = sum(rolls)
        (S + Diff)/(n+m) == mean
        Diff = (mean*(n+m))-S
        '''
        diff = (mean*(n+len(rolls)))-sum(rolls)
        if (diff / n) < 1 or (diff / n) > 6: return []

        missing = []
        ele = 6
        while diff > 0:
            # print(diff, ele, n)
            if (diff)-(n-1) >= ele:
                missing.append(ele)
                diff -= ele
                n -= 1
            else:
                ele -= 1
        
        return missing
        
        