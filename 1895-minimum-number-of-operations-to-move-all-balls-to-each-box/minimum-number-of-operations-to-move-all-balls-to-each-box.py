class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        balls_left = 0
        moves_left = 0 
        balls_right = 0
        moves_right = 0

        ans = [0]*n
        for i in range(n):
            moves_left += balls_left
            balls_left += (boxes[i] == '1')
            ans[i] += moves_left
        
        for i in range(n-1, -1, -1):
            moves_right += balls_right
            balls_right += (boxes[i] == '1')
            ans[i] += moves_right
        
        return ans