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
        for i in range(m):
            ans += max(sum_cols[i], n - sum_cols[i]) * (1 << m - 1 - i)
        return ans
