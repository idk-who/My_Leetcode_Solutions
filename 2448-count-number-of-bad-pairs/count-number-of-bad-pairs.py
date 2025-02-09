class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        data = defaultdict(int)
        data[nums[0]-0] = 1
        for j in range(1, len(nums)):
            ans += (j - data[nums[j]-j])
            data[nums[j]-j] += 1
        return ans