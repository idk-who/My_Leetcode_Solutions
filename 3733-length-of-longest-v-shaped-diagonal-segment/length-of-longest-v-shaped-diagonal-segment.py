class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        grid = grid
        dp = dict()
        n, m = len(grid), len(grid[0])

        def dfs(i, j, dir, made_turn = False, prev = -1):
            if 0 <= i < n and 0 <= j < m and grid[i][j] != 1 and grid[i][j] != prev:
                if (i, j, dir, made_turn) in dp:
                    return dp[(i, j, dir, made_turn)]
                else:
                    org = grid[i][j]
                    grid[i][j] = 1
                    new_dir = {
                        (-1, -1):(-1, 1),
                        (-1, 1) :(1, 1),
                        (1, 1)  :(1, -1),
                        (1, -1) :(-1, -1)
                    }[dir]
                    dp[(i, j, dir, made_turn)] = 1 + max(
                        dfs(i+dir[0], j+dir[1], dir, made_turn, org),
                        dfs(
                            i+new_dir[0], j+new_dir[1], new_dir, True, org
                        ) if not made_turn else 0
                    )
                    grid[i][j] = org
                    return dp[(i, j, dir, made_turn)]
            else:
                return 0

        ma = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ma = max(
                        ma,
                        1 + max(
                            dfs(i-1, j-1, (-1, -1), prev = 0),
                            dfs(i-1, j+1, (-1, +1), prev = 0),
                            dfs(i+1, j-1, (+1, -1), prev = 0),
                            dfs(i+1, j+1, (+1, +1), prev = 0)
                        )
                    )
                    print(i, j, ma)
        return ma
