class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ma = max(nums)

        count = [0] * (ma+1)

        for num in nums:
            count[max(num-k, 0)] += 1
            if num + k + 1 <= ma:
                count[num+k+1] -= 1
        
        ans = 0
        su = 0

        for val in count:
            su += val
            ans = max(ans, su)
        
        return ans



        

