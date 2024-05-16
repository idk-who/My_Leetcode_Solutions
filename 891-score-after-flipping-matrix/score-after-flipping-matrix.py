class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        sum_cols = [0]*m
        for row in grid:
            if row[0]:
                for i in range(m):
                    sum_cols[i] += row[i]
            else:
                for i in range(m):
                    sum_cols[i] += 0 if row[i] else 1                 
                    
        ans = 0
        tows = 1
        for i in range(m):
            ans += tows*sum_cols[m-i-1] if sum_cols[m-i-1]>n/2 else tows*(n - sum_cols[m-i-1])
            tows *= 2
        return ans