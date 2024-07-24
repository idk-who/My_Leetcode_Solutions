class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]

        def DFS(node, parent, visited):
            visited[node] = True
            for v in adj[node]:
                if not visited[v]:
                    if DFS(v, node, visited):
                        return True
                elif v != parent:
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [False]*(len(edges)+1)
            if DFS(u, v, visited):
                return [u, v]
        
        return [-1, -1]

