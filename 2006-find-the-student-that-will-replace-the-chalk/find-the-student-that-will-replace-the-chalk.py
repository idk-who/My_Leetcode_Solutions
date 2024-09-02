class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        su = sum(chalk)
        k = k % su

        for i in range(len(chalk)):
            if chalk[i] <= k:
                k -= chalk[i]
            else:
                return i

        return -1