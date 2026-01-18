class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        start = list(start)
        adj = [[] for i in range(len(start))]
        edge_ind = {}
        for ind, (u, v) in enumerate(edges):
            edge_ind[(u, v)] = ind
            edge_ind[(v, u)] = ind
            adj[u].append(v)
            adj[v].append(u)
        
        ans = []
        visited = set()
        def dfs(parent, u):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(u, v)
            
            if start[u] != target[u] and u != parent:
                ans.append(edge_ind[(parent, u)])
                start[u] = '1' if start[u] == '0' else '0'
                start[parent] = '1' if start[parent] == '0' else '0'
            
            # print(parent, u, start)

        dfs(0, 0)

        if start[0] != target[0]:
            return [-1]
        return list(sorted(ans))