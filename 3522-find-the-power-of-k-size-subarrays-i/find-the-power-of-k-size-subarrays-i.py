class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cons = k
        prev = float("-inf")
        ans = []
        for i, ele in enumerate(nums):
            if prev == float("-inf") or prev+1 == ele:
                cons -= 1
                prev = ele
            else:
                prev = ele
                cons = k-1
                
            if i >= k-1:
                if cons <= 0:
                    ans.append(ele)
                else:
                    ans.append(-1)
            
        return ans
                