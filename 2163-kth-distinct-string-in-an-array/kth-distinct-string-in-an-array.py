class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str: 
        f = Counter(arr)
        
        for s, v in f.items():
            if v == 1:
                k -= 1
            if k == 0:
                return s
        
        return ""
