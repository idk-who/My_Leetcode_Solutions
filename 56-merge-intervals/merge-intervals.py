class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        merged = []
        for u, v in intervals:
            if not merged or merged[-1][1] < u:
                merged.append([u, v])
            else:
                merged[-1][1] = max(merged[-1][1], v)
        
        return merged