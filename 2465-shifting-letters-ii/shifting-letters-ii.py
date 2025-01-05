class Solution:
    def shiftingLetters(self, string: str, shifts: List[List[int]]) -> str:
        n = len(string)
        lazy_compute = [0]*n

        for s, e, d in shifts:
            d = 1 if d else -1
            lazy_compute[s] += d
            if e+1 < n:
                lazy_compute[e+1] -= d

        def get_char(c, diff):
            return chr(
                (
                    ord(c)-ord('a')+diff
                )%26
                + ord('a')
            )
        
        ans = [""]*n
        diff = 0
        for i in range(n):
            diff += lazy_compute[i]
            ans[i] = get_char(
                string[i],
                diff
            )

        return "".join(ans)