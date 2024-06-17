squares = []

for i in range(46342):
    squares.append(i**2)

ssquares = set(squares)

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ptr = 0

        while squares[ptr] <= c:
            if c - squares[ptr] in ssquares:
                # print(squares[ptr])
                return True

            ptr += 1
        
        return False
