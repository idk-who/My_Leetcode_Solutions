class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]

        head = 0
        while head != slow:
            head = nums[head]
            slow = nums[slow]

        return slow

