class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        one = nums[0]
        two = max(nums[1], one)

        for i in range(2, n-1):
            two, one = max(nums[i]+one, two), two
        
        ans1 = two

        one = nums[1]
        two = max(nums[2], one)

        for i in range(3, n):
            two, one = max(nums[i]+one, two), two   
        
        ans2 = two

        return max(ans1, ans2)
