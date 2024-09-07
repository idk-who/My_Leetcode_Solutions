class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        s = set()
        is_odd = (n&1)
        le = n//2+(n&1)
        def creat_num(i):
            num = str(i)
            if is_odd:
                num += str(i)[:-1][::-1]
            else:
                num += str(i)[::-1]
            # print(num)
            return int(num)
        print((10**(le-1), 10**le))
        for i in range(10**(le-1), 10**le):
            num = creat_num(i)
            if num % k == 0:
                # print("".join(sorted(list(str(num)))))
                s.add("".join(sorted(str(num))))
        ans = 0
        print(s)
        for i in s:
            cnt = Counter(i)
            temp = (n-cnt['0']) * factorial(n-1)
            for _, j in cnt.items():
                temp //= factorial(j)
            ans += temp
        return ans
        
        