class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        ts = 0  #total sum

        for i in range(len(arr)):
            ts += arr[i]
            if ts == (i*(i+1))/2:
                ans += 1
        
        return ans



