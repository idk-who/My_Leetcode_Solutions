class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        adj = [[float("inf")]*26 for i in range(26)]
        off = ord('a')
        for i in range(n):
            adj[ord(original[i])-off][ord(changed[i])-off] = min(
                adj[ord(original[i])-off][ord(changed[i])-off],
                cost[i]
            )
        
        for i in range(26):
            adj[i][i] = 0

        for k in range(26):
            for u in range(26):
                for v in range(26):
                    adj[u][v] = min(
                        adj[u][v],
                        adj[u][k] + adj[k][v]
                    )

        for u in range(26):
            for v in range(26):
                if adj[u][v] == float("inf"):
                    adj[u][v] = -1

        total_cost = 0

        for s, t in zip(source, target):
            if adj[ord(s)-off][ord(t)-off] == -1: return -1
            total_cost += adj[ord(s)-off][ord(t)-off]
        return total_cost