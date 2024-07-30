class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                head = 0
                while slow != head:
                    slow = nums[slow]
                    head = nums[head]
                return head
        
        return -1