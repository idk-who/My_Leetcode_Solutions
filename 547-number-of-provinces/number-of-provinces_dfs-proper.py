class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(node):
            visited[node] = True
            for n2 in range(n):
                if not visited[n2] and isConnected[node][n2]:
                    dfs(n2)

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)

        return ans
