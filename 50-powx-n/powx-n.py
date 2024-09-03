class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        dp = dict()

        def pow(x, n, dp):
            if n == 0: return 1
            if n == 1: return x
            if n == -1: return 1/x
            if n in dp:
                return dp[n]
            ans = pow(x, n//2, dp) * pow(x, n//2+(n&1), dp)
            dp[n] = ans
            return ans
        
        return pow(x, n, dp)


