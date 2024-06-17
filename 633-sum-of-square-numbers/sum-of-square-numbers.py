class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c)) + 1):
            if self.hasIntegerRoot(c - i ** 2):
                return True
        return False

    def hasIntegerRoot(self, n):
        low, high = 0, int(sqrt(n)) + 1
        while low <= high:
            mid = low + (high - low) // 2
            if mid ** 2 == n:
                return True
            elif mid ** 2 > n:
                high = mid - 1
            else:
                low = mid + 1

        return False
