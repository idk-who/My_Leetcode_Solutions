class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        def DFS(graph, visited, node, color):
            # print(node)
            if visited[node] != 0:
                if visited[node] == color:
                    return True
                else:
                    return False
            
            visited[node] = color

            ans = True
            for v in graph[node]:
                ans &= DFS(graph, visited, v, -color)
            
            return ans

        ans = True
        for i in range(len(graph)):
            if visited[i] == 0:
                ans &= DFS(graph, visited, i, 1)
        
        return ans