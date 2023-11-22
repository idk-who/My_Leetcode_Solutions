class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        max_h = 0
        count = 0
        for i in citations:
            count+=1
            max_h = max(max_h, min(count, i))
                 
        return max_h
