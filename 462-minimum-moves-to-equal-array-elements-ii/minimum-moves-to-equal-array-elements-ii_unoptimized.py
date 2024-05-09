class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        num = nums[0]
        cost = 0
        for i in nums:
            cost += num-i
        _min = cost
        for i in range(1, len(nums)):
            new_num = nums[i]
            cost = cost - (((len(nums)-i))*(num-new_num)) + (num-new_num)*i
            _min = min(cost, _min)
            num = new_num
        
        return _min
