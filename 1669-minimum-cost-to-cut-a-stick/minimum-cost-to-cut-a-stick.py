class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = dict()
        
        def rec(cuts, i, j, dp):
            if j - i == 1:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            mi = float('inf')
            for k in range(i+1, j):
                mi = min(
                    mi,
                    cuts[j] - cuts[i] + (
                        rec(cuts, i, k, dp) + 
                        rec(cuts, k, j, dp)
                    )
                )
            dp[(i, j)] = mi
            
            return mi
        
        return rec(cuts, 0, len(cuts)-1, dp)
