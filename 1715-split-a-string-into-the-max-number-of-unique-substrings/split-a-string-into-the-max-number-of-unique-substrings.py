class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # dp = {}

        def rec(ptr, se):
            if ptr == len(s):
                return 0
            
            ma = float('-inf')
            for i in range(ptr+1, len(s)+1):
                if s[ptr:i] not in se:
                    se.add(s[ptr:i])
                    ma = max(
                        ma,
                        1 + rec(i, se)
                    )
                    se.remove(s[ptr:i])
            return ma
        
        return rec(0, set())
        