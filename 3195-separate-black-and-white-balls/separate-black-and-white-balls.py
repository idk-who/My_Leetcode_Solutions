class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cnt_bb = 0

        for ele in s:
            if ele == '0':
                ans += cnt_bb
            else:
                cnt_bb += 1
        
        return ans
