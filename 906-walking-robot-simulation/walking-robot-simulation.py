class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        h = 0
        pos = (0, 0)

        obstacles = {(i,j) for i, j in obstacles}

        furthest = 0

        for c in commands:
            if c == -1:
                h = (h+1)%4
            elif c == -2:
                h = (h-1)%4
            else:
                while c and ((pos[0]+dirs[h][0], pos[1]+dirs[h][1]) not in obstacles):
                    c -= 1
                    pos = (pos[0]+dirs[h][0], pos[1]+dirs[h][1])
                furthest = max(
                    furthest,
                    pos[0]*pos[0] + pos[1]*pos[1]
                )

        return furthest
