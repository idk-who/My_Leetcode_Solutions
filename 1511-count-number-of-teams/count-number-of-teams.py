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
        n = len(rating)
        lft = FT(n)
        rft = FT(n)

        temp = sorted([(r, i) for i, r in enumerate(rating)])
        ind_map = [0]*n
        for i, (_, ind) in enumerate(temp): ind_map[ind] = i

        for r in ind_map: rft.update(r, 1)
        
        cnt = 0
        for r in ind_map:
            rft.update(r, -1)

            ll = lft.query(r)
            lg = lft.query(n)-lft.query(r+1)
            rl = rft.query(r)
            rg = rft.query(n)-rft.query(r+1)

            cnt += (ll*rg)+(lg*rl)

            lft.update(r, 1)
        
        return cnt