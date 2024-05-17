import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        left = 0
        right = 1
        
        while left <= right:
            mid = left + (right-left)/2

            j, total, num, den = 1, 0, 0, 0
            maxFrac = 0
            for i in range(n):
                while j<n and arr[i] >= arr[j] * mid:
                    j += 1
                if j == n: break
                
                total += n - j 

                if maxFrac < arr[i] / arr[j]:
                    maxFrac = arr[i] / arr[j]
                    num, den = i, j
            
            if total == k:
                return [arr[num], arr[den]]
            
            if total > k:
                right = mid
            else:
                left = mid
        
