class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ptr = 1
        prev_su1_len = 0
        ans = float('-inf')
        while ptr < len(nums):
            print(ptr)
            ptr -= 1
            p1_ = p1 = next_ptr = ptr
            while p1+1 < len(nums) and nums[p1+1] > nums[p1]:
                p1 += 1
                next_ptr += 1
            max_su1 = 0
            if p1 > ptr:
                max_su1 = su1 = nums[p1] + nums[p1-1]
                p1 -= 2
                while p1 >= p1_:
                    su1 += nums[p1]
                    max_su1 = max(
                        max_su1, su1
                    )
                    p1 -= 1

            su1_len = next_ptr - ptr

            p2 = next_ptr
            su2 = 0
            while p2+1 < len(nums) and nums[p2+1] < nums[p2]:
                su2 += nums[p2+1]
                p2 += 1
                next_ptr += 1
            su2 -= nums[p2]
            ptr = next_ptr + 1
            
            if ptr < len(nums) and nums[ptr] == nums[ptr-1]:
                ptr += 1
                continue
            if ptr < len(nums):
                p3 = ptr
                max_su3 = su3 = nums[next_ptr] + nums[ptr]
                while p3+1 < len(nums) and nums[p3+1] > nums[p3]:
                    su3 += nums[p3+1]
                    p3 += 1
                    max_su3 = max(
                        max_su3,
                        su3
                    )

            if su1_len > 0 and p3 >= ptr:
                print(max_su1, su2, max_su3, ptr)
                ans = max(
                    ans,
                    max_su1 + su2 + max_su3
                )
        return ans
