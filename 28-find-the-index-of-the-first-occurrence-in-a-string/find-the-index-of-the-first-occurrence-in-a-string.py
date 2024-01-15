class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            j = i
            k = 0
            while k < n and haystack[j] == needle[k]:
                j += 1
                k += 1
            if j == i+n:
                return i
        return -1