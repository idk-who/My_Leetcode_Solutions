class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]

        uf = UnionFind(len(edges)+1)
        
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        
        return [-1, -1]

