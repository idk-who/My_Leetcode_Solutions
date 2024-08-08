class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        p_di = 0

        ans = [(rStart, cStart)]

        iterations = max(
            abs(rStart - rows),
            abs(rStart - 0),
            abs(cStart - cols),
            abs(cStart - 0)
        )

        cnt = 1
        i, j = rStart, cStart

        for __ in range(iterations+1):
            for _ in range(cnt):
                i, j = i+di[p_di][0], j+di[p_di][1] 
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
            p_di += 1
            for _ in range(cnt):
                i, j = i+di[p_di][0], j+di[p_di][1]
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
            p_di += 1
            cnt += 1

            for _ in range(cnt):
                i, j = i+di[p_di][0], j+di[p_di][1]
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
            p_di += 1
            for _ in range(cnt):
                i, j = i+di[p_di][0], j+di[p_di][1]
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
            p_di += 1
            cnt += 1

            p_di = 0
        
        return ans
