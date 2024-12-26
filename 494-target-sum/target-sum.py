class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        count[0] = 1

        for i in nums:
            next = defaultdict(int)
            for j in count:
                next[j-i] += count[j]
                next[j+i] += count[j]
            count = next
        
        return count[target]