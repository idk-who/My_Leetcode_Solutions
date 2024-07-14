class Solution:
    def countOfAtoms(self, formula: str) -> str:
        asdf = 0 
        def helper(formula, ptr, n) -> dict:
            # nonlocal asdf
            d = defaultdict(int)
            while ptr < n:
                # print(ptr, n)
                # if asdf > 30: exit()
                # asdf += 1
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
                    s = ["("]
                    ptr += 1
                    while len(s) != 0:
                        if formula[ptr] == '(':
                            s.append('(')
                        elif formula[ptr] == ')':
                            s.pop()
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
            # print(d)
            return d

        atoms = sorted([k, str(v) if v != 1 else ''] for k, v in helper(formula, 0, len(formula)).items())
        return "".join([ele for pair in atoms for ele in pair])

