class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # if len(edges) < n - 1: return -1
        teams = [0]*n
        adj = [[] for i in range(n)]
        for u, v in edges:
            teams[v] += 1
            adj[u].append(v)
        if teams.count(0) > 1: 
            return -1
        return teams.index(0)
        # def helper(u):
        #     cnt = 0
        #     for v in adj[u]:
        #         cnt += 1 + helper(v)
        #     return cnt

        # for i in range(n):
        #     if teams[i] == 0:
        #         if helper(i) == len(edges):
        #             return i
        
        # return -1