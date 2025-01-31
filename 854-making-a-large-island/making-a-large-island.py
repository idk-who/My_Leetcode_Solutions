class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def calc_size(grid, i, j, island_id):
            if 0<=i<n and 0<=j<n and grid[i][j] == 1:
                grid[i][j] = island_id
                return (
                    1 +
                    calc_size(grid, i-1, j, island_id) +
                    calc_size(grid, i+1, j, island_id) +
                    calc_size(grid, i, j-1, island_id) +
                    calc_size(grid, i, j+1, island_id)
                )
            return 0
        
        island_sizes = dict()
        island_id = 2

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = calc_size(
                        grid, i, j, island_id
                    )
                    island_id += 1

        if len(island_sizes) == 0:
            return 1
        
        if len(island_sizes) == 1:
            return min(island_sizes[island_id-1]+1, n*n)


        def get_neighbours(i, j):
            neighbours = set()
            for _i, _j in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                if 0<=_i<n and 0<=_j<n and grid[_i][_j] > 0:
                    neighbours.add(grid[_i][_j])
            return neighbours

        max_size = 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    curr_size = 1

                    neighbours = get_neighbours(i, j)
                    
                    for island_id in neighbours:
                        curr_size += island_sizes[island_id]
                    
                    max_size = max(max_size, curr_size)
                    
        return max_size


        