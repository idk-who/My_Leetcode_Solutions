class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        sum_ = 0
        for ind, ele in enumerate(nums):
            sum_ = (sum_ + ele) % k
            if sum_ in d:
                if ind - d[sum_] >= 2:
                    return True
            else:
                d[sum_] = ind
        
        return False
