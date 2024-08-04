class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_till_first_neg = 1
        first_neg_ind = -1
        prod = 1
        ans = nums[0]

        for ind, i in enumerate(nums):
            prod *= i
            if prod_till_first_neg > 0:
                prod_till_first_neg *= i
                first_neg_ind = ind
            if i == 0:
                prod_till_first_neg = 1
                first_neg_ind = -1

            
            if prod < 0:
                ans = max(ans, prod//prod_till_first_neg if first_neg_ind != ind else prod)
            else:
                ans = max(ans, prod)
            
            if prod == 0:
                prod = 1
        
        return ans

            
