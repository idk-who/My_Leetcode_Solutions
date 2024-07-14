class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def helper(formula, ptr, n) -> dict:
            d = defaultdict(int)
            while ptr < n:
                if formula[ptr].isupper():
                    name = formula[ptr]
                    ptr += 1
                    while ptr < n and formula[ptr].islower():
                        name += formula[ptr]
                        ptr += 1
                    count = 0
                    while ptr < n and formula[ptr].isdigit():
                        count = count*10 + int(formula[ptr])
                        ptr += 1
                    if count == 0: count = 1
                    d[name] += count
                elif formula[ptr] == '(':
                    nptr = ptr + 1
                    ns = 1
                    ptr += 1
                    while ns != 0:
                        if formula[ptr] == '(':
                            ns += 1
                        elif formula[ptr] == ')':
                            ns -= 1
                        ptr += 1
                    nn = ptr - 1 

                    newd = helper(formula, nptr, nn)

                    count = 0
                    while ptr < n and formula[ptr].isdigit():
                        count = count*10 + int(formula[ptr])
                        ptr += 1
                    if count == 0: count = 1
                    for k in newd:
                        newd[k] *= count
                    
                    for k in newd:
                        d[k] += newd[k]
            return d

        atoms = sorted([k, str(v) if v != 1 else ''] for k, v in helper(formula, 0, len(formula)).items())
        return "".join([ele for pair in atoms for ele in pair])

