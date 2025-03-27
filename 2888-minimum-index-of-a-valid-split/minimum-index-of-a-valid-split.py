class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dom_ele = -1
        cnt = 0
        for i in nums:
            if i == dom_ele:
                cnt += 1
            else:
                cnt -= 1
            if cnt <= 0:
                dom_ele = i
                cnt = 1
        # print(dom_ele)

        dom_ele_cnt = 0
        for i in nums:
            if i == dom_ele:
                dom_ele_cnt += 1


        l_cnt = 0
        r_cnt = dom_ele_cnt

        for i in range(len(nums)):
            if nums[i] == dom_ele:
                l_cnt += 1
                r_cnt -= 1

            if l_cnt > (i+1)/2 and r_cnt > (len(nums)-i-1)/2:
                return i
            # print(l_cnt, r_cnt)

        return -1 