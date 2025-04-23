class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        ma = -1

        for i in range(1, n+1):
            su = 0
            while i:
                su += i%10
                i //= 10
            d[su] += 1
            ma = max(ma, d[su])
        
        ans = 0
        for k, v in d.items():
            if v == ma:
                ans += 1

        return ans