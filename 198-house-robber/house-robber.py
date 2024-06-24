class Solution:
    def rob(self, A):
        if len(A) <= 2:
            return max(A)
        one = A[0]
        two = max(one, A[1])
        three = max(one + A[2], two)

        for i in range(3, len(A)):
            three, two, one = max(A[i] + two, three), three, two
            print(three)
        
        return three