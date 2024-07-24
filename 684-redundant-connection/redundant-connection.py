class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def BFS(node, par):
            visited = set([node])
            q = deque([(node, par)])
            while q:
                node, parent = q.popleft()
                for v in adj[node]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, node))
                    elif v != parent:
                        return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            if BFS(u, v):
                return [u, v]
        
        return [-1, -1]

