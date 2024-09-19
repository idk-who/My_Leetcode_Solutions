class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        d = dict()

        def rec(exp, l, r):
            if l > r:
                return [0]
            if l == r or (l + 1 == r and exp[l:r+1].isdigit()):
                return [int(exp[l:r+1])]

            total_poss = []

            for k in range(l, r+1):
                if exp[k] in ['-','+','*']:
                    sym = exp[k]
                    poss_l = rec(exp, l, k-1)
                    poss_r = rec(exp, k+1, r)

                    for i in poss_l:
                        for j in poss_r:
                            if sym == '-':
                                total_poss.append(i-j)
                            elif sym == '+':
                                total_poss.append(i+j)
                            else:
                                total_poss.append(i*j)
            
            return total_poss
        
        return rec(expression, 0, len(expression)-1)





