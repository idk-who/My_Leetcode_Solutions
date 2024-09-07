class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        is_odd = (n&1)
        def creat_num(i):
            num = str(i)
            num += str(i)[::-1][is_odd:]
            return num

        s = set()
        le = n//2+(n&1)
        for i in range(10**(le-1), 10**le):
            num = creat_num(i)
            if int(num) % k == 0:
                s.add("".join(sorted(num)))

        ans = 0
        for i in s:
            cnt = Counter(i)
            perms = (n-cnt['0']) * factorial(n-1)
            for _, j in cnt.items():
                perms //= factorial(j)
            ans += perms
        return ans
        
        