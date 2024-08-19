class Solution:
    def minSteps(self, n: int) -> int:
        div = n//2
        ops = 0
        while n > 1:
            # print(div, n)
            if n%div == 0:
                # ops += 1
                ops += n//div
                n = div
            div -= 1
        
        return ops