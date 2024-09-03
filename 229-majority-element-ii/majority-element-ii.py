class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1 = None
        cnt1 = 0
        ele2 = None
        cnt2 = 0

        for i in nums:
            if i == ele1:
                cnt1 += 1
            elif i == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = i
                cnt1 += 1
            elif cnt2 == 0:
                ele2 = i
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        return [i for i in (ele1, ele2) if nums.count(i) > len(nums)/3]

        