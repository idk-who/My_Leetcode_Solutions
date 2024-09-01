class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow: break

        head = 0
        while head != slow:
            head = nums[head]
            slow = nums[slow]

        return head

