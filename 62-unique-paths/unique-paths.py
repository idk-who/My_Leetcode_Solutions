class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n: m, n = n, m

        ans = 1
        j = 1
        for i in range(m+n-2, m-1, -1):
            ans = (ans * i) // j
            j += 1

        return ans