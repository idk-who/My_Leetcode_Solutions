class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        s = 0
        ans = 0
        for i in nums:
            s = (s+i) % k
            if s in d:
                ans += d[s]
                d[s] += 1
            else:
                d[s] = 1
        
        return ans
