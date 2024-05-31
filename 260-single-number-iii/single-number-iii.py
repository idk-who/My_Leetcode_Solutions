class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        
        ans = []

        for i in d:
            if d[i] == 1:
                ans.append(i)

        return ans