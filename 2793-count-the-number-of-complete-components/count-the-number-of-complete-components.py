class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def rec(u):
            visited.add(u)
            nodes = 1
            edges = len(adj[u])

            for v in adj[u]:
                if v not in visited:
                    n, e = rec(v)
                    nodes += n
                    edges += e 
            # print(u, nodes, edges)
            return nodes, edges
        
        def su(n):
            return (n*(n-1))//2

        ans = 0
        
        visited = set()
        for i in range(n):
            if i not in visited:
                nodes, edges = rec(i)
                # print("MAIN", i, nodes, edges, su(nodes))
                if edges//2 == su(nodes):
                    # print("ADD", i)
                    ans += 1
    
        return ans