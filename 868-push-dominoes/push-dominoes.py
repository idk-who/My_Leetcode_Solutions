class Solution:
    def pushDominoes(self, s: str) -> str:
        return re.sub(r'(?<=R)(\.+)(?=L)',lambda m:(q:=len(m[1]))//2*'R'+q%2*'.'+q//2*'L',re.sub(r'(R|L)(\.+)(?=\1)',lambda m:m[1]*(len(m[2])+1),f'L{s}R'))[1:-1]