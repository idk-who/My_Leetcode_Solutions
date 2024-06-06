class UnionFind(object):
    def __init__(self, n):
        self.u = list(range(n))
        
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.u[ra] = rb
    
    def find(self, a):
        while self.u[a] != a: a = self.u[a]
        return a
    
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        if not M: return 0
        s = len(M)
        
        uf = UnionFind(s)
        for r in range(s):
            for c in range(r,s):
                if M[r][c] == 1: uf.union(r,c)
                    
        return len(set([uf.find(i) for i in range(s)]))