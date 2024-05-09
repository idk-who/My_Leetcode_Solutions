import heapq
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _max, _sum = max(milestones), sum(milestones)

        if _max <= _sum - _max:
            return _sum
        
        return 2*(_sum - _max)+1


