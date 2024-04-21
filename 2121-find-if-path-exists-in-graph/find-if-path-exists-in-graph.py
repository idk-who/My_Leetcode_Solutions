class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edgesd = [[] for _ in range(n)]
        for i, j in edges:
            edgesd[i].append(j)
            edgesd[j].append(i)

        stack = [source]
        visited = [False]*n
        visited[source] = True

        while stack:
            node = stack.pop()

            if node == destination:
                return True
            
            for i in edgesd[node]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
        
        return False
            