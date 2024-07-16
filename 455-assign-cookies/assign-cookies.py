class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content = 0
        gPtr, sPtr = 0, 0
        while gPtr < len(g) and sPtr < len(s):
            if s[sPtr] >= g[gPtr]:
                gPtr += 1
            sPtr += 1
        
        return gPtr