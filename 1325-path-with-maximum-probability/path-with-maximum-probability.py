from heapq import heappop, heappush

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]

        for i in range(len(edges)):
            u, v = edges[i]
            wt = succProb[i]
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        dist = [float("-inf")]*n
        dist[start_node] = 1
        h = [(start_node, 1)]
        # print(adj)
        while h:
            # print(h)
            u, p = heappop(h)

            for v, np in adj[u]:
                if dist[v] < p*np:
                    dist[v] = p*np
                    heappush(h, (v, p*np))
                
        return dist[end_node] if dist[end_node] != float("-inf") else 0
