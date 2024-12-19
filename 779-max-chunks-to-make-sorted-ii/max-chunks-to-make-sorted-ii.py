class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)

        prefixMax = [0]*len(arr)
        ma = float('-inf')
        for i in range(n):
            ma = max(arr[i], ma)
            prefixMax[i] = ma

        suffixMin = [0]*len(arr)
        mi = float('inf')
        for i in range(n-1, -1, -1):
            mi = min(arr[i], mi)
            suffixMin[i] = mi

        chunks = 1
        for i in range(1, n):
            if suffixMin[i] >= prefixMax[i-1]:
                chunks += 1
        
        return chunks


        