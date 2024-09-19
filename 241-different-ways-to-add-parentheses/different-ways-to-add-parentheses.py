class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expr = expression

        def rec(l, r):
            if l > r:
                return [0]
            if l == r or (l + 1 == r and expr[l:r+1].isdigit()):
                return [int(expr[l:r+1])]

            total_poss = []

            for k in range(l, r+1):
                if expr[k] in ['-','+','*']:
                    sym = expr[k]
                    poss_l = rec(l, k-1)
                    poss_r = rec(k+1, r)

                    for i in poss_l:
                        for j in poss_r:
                            if sym == '-':
                                total_poss.append(i-j)
                            elif sym == '+':
                                total_poss.append(i+j)
                            else:
                                total_poss.append(i*j)
            
            return total_poss
        
        return rec(0, len(expr)-1)





