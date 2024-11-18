class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        elif k < 0:
            step = -1
        else:
            step = 1
        ans = []
        for i in range(n):
            temp = 0
            for j in range(i+step, i + (k+1*step), step):
                temp += code[j%n]
            ans.append(temp)

        return ans