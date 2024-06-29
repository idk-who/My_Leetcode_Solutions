class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[v].append(u)
        
        ancestors = [[] for _ in range(n)]

        def dfs(node):
            if len(ancestors[node]) != 0:
                return ancestors[node]
            
            ancestor = set()
            for u in adj_list[node]:
                ancestor.add(u)
                ancestor.update(dfs(u))
            
            ancestors[node] = sorted(list(ancestor))
            return ancestors[node]
        
        for i in range(n):
            dfs(i)

        return ancestors