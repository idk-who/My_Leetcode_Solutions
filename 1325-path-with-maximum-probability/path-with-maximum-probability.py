from heapq import heappop, heappush

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]

        for i in range(len(edges)):
            u, v = edges[i]
            wt = succProb[i]
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        dist = [0]*n
        dist[start_node] = 1
        h = [(-1, start_node)]
        while h:
            p, u = heappop(h)

            for v, np in adj[u]:
                if dist[v] < -p*np:
                    dist[v] = -p*np
                    heappush(h, (p*np, v))
                
        return dist[end_node] 
