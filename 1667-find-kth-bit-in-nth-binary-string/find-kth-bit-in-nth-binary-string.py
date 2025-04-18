class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ptr = 0
        sn = [False]
        
        for i in range(1, n+1):
            sn.append(True)
            sn.extend(list(reversed(list(map(lambda x: not x, sn[:-1])))))
        
        return '1' if sn[k-1] else '0'