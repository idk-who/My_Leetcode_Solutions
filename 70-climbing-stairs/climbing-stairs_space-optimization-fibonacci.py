class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return 1

        prev = next = 1
        for i in range(2, n+1):
            prev, next = next, prev + next
        
        return next
