class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rem = time % (n-1)
        q = time // (n-1)

        if q&1:
            return n-rem
        else:
            return rem + 1