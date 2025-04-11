class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            if not (len(str(i))&1):
                if i < 100:
                    if i//10 == i%10:
                        ans += 1
                else:
                    if i // 1000 + (i % 1000 // 100) == i % 100 // 10 + i % 10:
                        ans += 1
                
        return ans