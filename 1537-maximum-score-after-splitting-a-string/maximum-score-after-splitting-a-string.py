class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        ones = 0
        for i in range(1, n):
            if s[i] == '1':
                ones += 1
        
        zeros = 1 if s[0] == '0' else 0

        score = zeros + ones
        for i in range(1, n-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(
                score,
                zeros + ones
            )
        
        return score