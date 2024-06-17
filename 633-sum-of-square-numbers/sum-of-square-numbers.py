class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = int(c**(1/2))

        if x * x == c:
            return True

        i, j = 0, x

        # two pointer
        while i <= j:
            find = c - (j * j)

            # Binary search
            l, h = i, j
            while l <= h:
                mid = l + (h - l) // 2
                if mid * mid == find:
                    return True
                if mid * mid < find:
                    l = mid + 1
                else:
                    h = mid - 1

            if (i * i) + (j * j) > c:
                j -= 1
            else:
                i += 1

        return False
