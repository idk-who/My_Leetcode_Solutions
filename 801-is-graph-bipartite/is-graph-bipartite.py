class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        def DFS(graph, visited, node, color):
            if visited[node] != 0:
                if visited[node] == color:
                    return True
                else:
                    return False
            
            visited[node] = color

            for v in graph[node]:
                if DFS(graph, visited, v, -color) == False:
                    return False
            
            return True

        for i in range(len(graph)):
            if visited[i] == 0:
                if DFS(graph, visited, i, 1) == False:
                    return False
        
        return True