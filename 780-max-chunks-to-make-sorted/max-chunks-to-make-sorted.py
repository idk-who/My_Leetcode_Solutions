class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        present = [0]*len(arr)
        ans = 0
        ts = 0  #total sum
        si = 0  #sum from prev till i

        for i in range(len(arr)):
            present[arr[i]] = 1

            # total sum
            ts += 1
            
            # collecting from past occurunces
            si += present[i]
            # collecting if past occurs
            if arr[i] < i:
                si += 1
                
            # print(ts, si)
            if si == ts == i + 1:
                ans += 1
        
        return ans