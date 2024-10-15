class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cnt_wb = 0

        for ind, ele in enumerate(s):
            if ele == '0':
                ans += (ind - cnt_wb)
                cnt_wb += 1
        
        return ans
