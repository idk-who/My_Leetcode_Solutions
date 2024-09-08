# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        le = 0
        temp = head
        while temp:
            le += 1
            temp = temp.next
        
        qu, re = le//k, le%k
    
        ans = []
        temp = head
        for _ in range(k):
            ans.append(temp)
            prev = None
            for i in range(qu+(re>0)):
                prev = temp
                temp = temp.next
            if prev: prev.next = None
            re -= 1
            
        return ans