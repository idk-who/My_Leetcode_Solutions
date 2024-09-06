# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        org_dummy = dummy
        nums = set(nums)

        while dummy and dummy.next:
            if dummy.next.val in nums:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        return org_dummy.next