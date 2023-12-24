class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hor = [1]
        hor.extend(sorted(hFences))
        hor.append(m)
        
        ver = [1]
        ver.extend(sorted(vFences))
        ver.append(n)
        
        hor_diff = set()
        for i in range(len(hor)):
            for j in range(i+1, len(hor)):
                temp = hor[j]-hor[i]
                hor_diff.add(temp)
        
        ans = -1
        for i in range(len(ver)):
            for j in range(i+1, len(ver)):
                temp = ver[j]-ver[i]
                if temp > ans and temp in hor_diff:
                    ans = temp
        
        if ans < 0:
            return -1
        else:
            return (ans**2)%(10**9 + 7)
                