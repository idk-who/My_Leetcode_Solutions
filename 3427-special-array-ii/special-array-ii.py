class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        starts = [0]
        for i in range(1, len(nums)):
            if (nums[i-1]&1) ^ (nums[i]&1):
                continue
            else:
                starts.append(i)
        
        ans = []
        for s, e in queries:
            p1 = bisect.bisect(starts, s)
            p2 = bisect.bisect(starts, e)
            ans.append(p1==p2)
        return ans