class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def BFS_topo(n, edges):
            adj = [[] for _ in range(n)]
            indegree = [0]*n

            for u, v in prerequisites:
                adj[v].append(u)
                indegree[u] += 1
            
            cnt = 0

            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    cnt += 1
                    q.append(i)
            
            while q:
                u = q.popleft()

                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        cnt += 1
                        q.append(v)
            
            return cnt == n

        return BFS_topo(numCourses, prerequisites)

        

