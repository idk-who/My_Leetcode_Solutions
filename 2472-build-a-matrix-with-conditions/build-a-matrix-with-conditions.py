from collections import deque

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        
        def make_order(conditions):
            indegree = [0]*(k+1)
            adj = [[] for i in range(k+1)]
            for u, v in conditions:
                indegree[v] += 1
                adj[u].append(v)
            
            q = deque([i for i in range(1, k+1) if indegree[i] == 0])
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            
            return order
        row_order = make_order(rowConditions)
        col_order = make_order(colConditions)
        
        if len(row_order) != k or len(col_order) != k:
            return []

        row_map = {num:ind for ind, num in enumerate(row_order)}
        col_map = {num:ind for ind, num in enumerate(col_order)}
        
        ans = [[0]*k for _ in range(k)]
        for i in range(1, k+1):
            ans[row_map[i]][col_map[i]] = i
        
        return ans

            

        