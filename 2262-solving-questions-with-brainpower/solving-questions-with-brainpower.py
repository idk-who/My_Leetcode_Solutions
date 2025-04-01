class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        dp = dict()
        def rec(ptr):
            if ptr >= n:
                return 0
            if ptr in dp:
                return dp[ptr]
            ma = max(
                rec(ptr+1),
                questions[ptr][0] + rec(ptr+1+questions[ptr][1])
            )
            dp[ptr] = ma
            return ma
        
        return rec(0)





