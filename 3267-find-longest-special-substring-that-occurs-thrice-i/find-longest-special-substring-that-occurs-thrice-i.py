class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)

        def is_special(string):
            c = string[0]
            for i in range(1, len(string)):
                if string[i] != c:
                    return False
            return True
            
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if is_special(s[i:j+1]):
                    d[s[i:j+1]] += 1
        
        ans = -1
        for k, v in d.items():
            if v >= 3:
                ans = max(ans, len(k))
        
        return ans