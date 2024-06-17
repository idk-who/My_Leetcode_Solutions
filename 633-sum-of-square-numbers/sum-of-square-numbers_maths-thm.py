# https://leetcode.com/problems/sum-of-square-numbers/solutions/5324398/beats-100-explained-with-video-c-java-python-js-maths-interview-solution/

class Solution(object):
    def judgeSquareSum(self, c):
        divisor = 2
        while divisor * divisor <= c:
            if c % divisor == 0:
                exponentCount = 0
                while c % divisor == 0:
                    exponentCount += 1
                    c //= divisor
                if divisor % 4 == 3 and exponentCount % 2 != 0:
                    return False
            divisor += 1
        return c % 4 != 3
