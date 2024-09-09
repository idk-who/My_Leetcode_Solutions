# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        n, m = m, n
        ans = [[-2]*m for _ in range(n)]

        def get_val():
            nonlocal head
            if head:
                v = head.val
                head = head.next
                return v
            else:
                return -1

        left = 0
        right = m-1
        up = 0
        down = n-1

        while left <= right and up <= down:
            # print("LOOP")
            for j in range(left, right+1):
                ans[up][j] = get_val()
            up += 1

            for i in range(up, down+1):
                ans[i][right] = get_val()
            right -= 1

            if up > down: break
            
            for j in range(right, left-1, -1):
                ans[down][j] = get_val()
            down -= 1

            if left > right: break

            for i in range(down, up-1, -1):
                ans[i][left] = get_val()
            left += 1
        
        return ans