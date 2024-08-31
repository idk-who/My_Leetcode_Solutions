class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        merged = []
        for u, v in intervals[1:]:
            if prev[1] >= u:
                prev[1] = max(prev[1], v)
            else:
                merged.append(prev)
                prev = [u, v]
        
        merged.append(prev)
        
        return merged