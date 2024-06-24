class Solution:
    def rob(self, A):
        if len(A) < 2:
            return A[0]
        one = A[0]
        two = max(one, A[1])

        for i in range(2, len(A)):
            two, one = max(A[i] + one, two), two
        
        return two