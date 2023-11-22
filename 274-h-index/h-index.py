class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations_count = [0] * (n+1)
        for i in citations:
            if i>=n:
                citations_count[n]+=1
            else:
                citations_count[i]+=1
        
        count = 0
        for i in range(n, -1, -1):
            count += citations_count[i]
            if i<=count:
                return i

        return count