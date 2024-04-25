class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        freq = [-1]*26
        s = map(lambda x:ord(x)-97, list(s))
        for i in s:
            m = 0
            for f in range(i-k, i+k+1):
                if f >= 0 and f < 26:
                    m = max(m, freq[f])
            freq[i] = m+1
        return max(freq)

