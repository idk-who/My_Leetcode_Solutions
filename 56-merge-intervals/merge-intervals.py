class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = None
        merged = []
        for u, v in intervals:
            if prev is None:
                prev = [u, v]
            elif prev[1] >= u:
                prev[1] = max(prev[1], v)
            else:
                merged.append(prev)
                prev = [u, v]
        
        if prev:
            merged.append(prev)
        
        return merged