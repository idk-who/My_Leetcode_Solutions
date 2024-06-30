class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n+1)]

        def find(i):
            if roots[i] == i: return i
            roots[i] = find(roots[i])
            return roots[i]

        def union(x, y):
            i, j = find(x), find(y)
            if i == j: return 0
            roots[i] = j
            return 1
        
        ans = t2 = t1 = 0

        for t, u, v in edges:
            if t == 3:
                if union(u, v):
                    t1 += 1
                    t2 += 1
                else:
                    ans += 1
        
        temp = roots[:]

        for t, u, v in edges:
            if t == 1:
                if union(u, v):
                    t1 += 1
                else:
                    ans += 1
        
        roots[:] = temp

        for t, u, v in edges:
            if t == 2:
                if union(u, v):
                    t2 += 1
                else:
                    ans += 1

        if t1 == t2 == n - 1:
            return ans
        return -1
        


