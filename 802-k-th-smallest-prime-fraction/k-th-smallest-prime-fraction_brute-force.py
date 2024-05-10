import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                ans.append((arr[i]/arr[j], arr[i], arr[j]))
        
        ans.sort()
        
        return [ans[k-1][1], ans[k-1][2]]
