class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        present = [0]*len(arr)

        ans = 0
        prev = 0
        for i in range(len(arr)):
            present[arr[i]] = 1
            # print(present)
            if sum(present[prev:i+1]) == sum(present[prev:]) == i - prev + 1:
                ans += 1
                prev = i + 1
        
        return ans