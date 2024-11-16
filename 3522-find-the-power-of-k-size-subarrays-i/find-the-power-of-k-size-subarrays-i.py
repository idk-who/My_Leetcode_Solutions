class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cons = k
        prev = 0
        ans = []
        for i, ele in enumerate(nums):
            if i == 0 or prev+1 == ele:
                cons -= 1
                prev = ele
            else:
                prev = ele
                cons = k-1
                
            if i + 1 >= k:
                if cons <= 0:
                    ans.append(ele)
                else:
                    ans.append(-1)
            
        return ans
                