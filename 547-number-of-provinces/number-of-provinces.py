class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, n):
        while self.parents[n] != n: 
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return
        if self.size[pa] > self.size[pb]:
            self.parents[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.parents[pa] = pb
            self.size[pb] += self.size[pa]
        self.count -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)

        return uf.count