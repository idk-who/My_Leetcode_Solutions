class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0]*len(colSum) for _ in range(len(rowSum))]
        n, m = len(rowSum), len(colSum)
        for i in range(n):
            for j in range(m):
                temp = min(rowSum[i], colSum[j])
                ans[i][j] = temp
                rowSum[i] -= temp
                colSum[j] -= temp
        return ans

