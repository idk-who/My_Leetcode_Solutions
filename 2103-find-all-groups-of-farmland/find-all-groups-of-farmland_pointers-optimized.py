class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []

        nr = len(land)
        nc = len(land[0])

        for r in range(nr):
            for c in range(nc):
                if land[r][c]:
                    if (r>0 and land[r-1][c]) or (c>0 and land[r][c-1]):
                        continue
                        
                    si, sj = r, c
                    ei, ej = r, c
                    while ei<nr and land[ei][sj]: ei += 1
                    while ej<nc and land[si][ej]: ej += 1

                    ans.append([si, sj, ei-1, ej-1])

        return ans
