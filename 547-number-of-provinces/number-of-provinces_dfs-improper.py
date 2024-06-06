class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        def dfs(i, j):
            isConnected[i][j] = 0
            for k in range(n):
                if isConnected[j][k]:
                    dfs(j, k)

        ans = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    ans += 1
                    dfs(i, j)
        
        return ans
