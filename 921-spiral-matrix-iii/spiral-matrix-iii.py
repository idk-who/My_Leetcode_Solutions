class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [(rStart, cStart)]
        iterations = max(
            abs(rStart - rows),
            abs(rStart - 0),
            abs(cStart - cols),
            abs(cStart - 0)
        )
        di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt = 1
        i, j = rStart, cStart

        for __ in range(iterations+1):
            for p_di in range(4):
                for _ in range(cnt):
                    i, j = i+di[p_di][0], j+di[p_di][1] 
                    if 0 <= i < rows and 0 <= j < cols:
                        ans.append([i, j])
                if p_di == 1 or p_di == 3:
                    cnt += 1
        
        return ans
