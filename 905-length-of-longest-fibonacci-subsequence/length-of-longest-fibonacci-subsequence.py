class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        eles = {i for i in arr}
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] in eles:
                    l = 2
                    a, b = arr[i], arr[j]
                    while a+b in eles:
                        a, b = b, a+b
                        l += 1
                    ans = max(
                        ans,
                        l
                    )
        return ans

            
            