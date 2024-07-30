class FT:
    def __init__(self, n):
        self.bit = [0]*n
    def update(self, ind, x):
        while ind < len(self.bit):
            self.bit[ind] += x
            ind |= ind + 1
    def query(self, end):
        ans = 0
        while end:
            ans += self.bit[end - 1]
            end &= end - 1
        return ans

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # fenwick tree without mask
        ma = max(rating)
        lft = FT(ma+1)
        rft = FT(ma+1)

        for r in rating: rft.update(r, 1)
        
        cnt = 0
        for r in rating:
            rft.update(r, -1)

            ll = lft.query(r)
            lg = lft.query(ma+1)-lft.query(r+1)
            rl = rft.query(r)
            rg = rft.query(ma+1)-rft.query(r+1)

            cnt += (ll*rg)+(lg*rl)

            lft.update(r, 1)
        
        return cnt