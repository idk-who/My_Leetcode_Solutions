class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alphas = ['a', 'b', 'c']
        def gen(n, i, prev, string):
            if i == n:
                yield "".join(string)
                return
            for w in alphas:
                if w != prev:
                    string.append(w)
                    yield from gen(n, i+1, w, string)
                    string.pop()
        
        ptr = 1
        
        for s in gen(n, 0, '', []):
            if ptr == k:
                return str(s)
            ptr += 1
        
        return ""