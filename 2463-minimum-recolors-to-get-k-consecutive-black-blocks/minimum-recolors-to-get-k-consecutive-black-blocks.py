class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        whites = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        
        mi_w = whites

        for i in range(k, n):
            if blocks[i-k] == 'W':
                whites -= 1
            if blocks[i] == 'W':
                whites += 1
            mi_w = min(mi_w, whites)
        
        return mi_w