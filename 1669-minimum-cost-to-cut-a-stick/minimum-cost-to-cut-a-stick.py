class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        
        def rec(r1, r2, cuts, i, j, dp):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            mi = float('inf')
            for k in range(i, j+1):
                mi = min(
                    mi,
                    r2-r1 + (
                        rec(r1, cuts[k], cuts, i, k-1, dp) + 
                        rec(cuts[k], r2, cuts, k+1, j, dp)
                    )
                )
            dp[(i, j)] = mi

            return mi
        
        return rec(0, n, cuts, 0, len(cuts)-1, dict())
