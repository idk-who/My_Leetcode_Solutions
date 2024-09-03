class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = []
        for i in s:
            n.append(str(ord(i)-ord('a')+1))
        n = int("".join(n))
        while k > 0 and n > 1:
            n = sum([int(i) for i in str(n)])
            k -= 1
        
        return n