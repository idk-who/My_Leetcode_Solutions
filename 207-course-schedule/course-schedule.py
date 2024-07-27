class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)

        visited = [False]*numCourses
        pathvis = [False]*numCourses

        def DFS(adj, node, vis, pvis):
            vis[node] = True
            pvis[node] = True

            for v in adj[node]:
                if not vis[v]:
                    if DFS(adj, v, vis, pvis):
                        return True
                elif pvis[v]:
                    return True
                
            pvis[node] = False
            return False

        for i in range(numCourses):
            if DFS(adj, i, visited, pathvis):
                return False
        return True

