class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            if not (len(str(i))&1):
                le = len(str(i))
                if sum([int(j) for j in str(i)[:le//2]]) == sum([int(j) for j in str(i)[le//2:]]):
                    ans += 1
        
        return ans