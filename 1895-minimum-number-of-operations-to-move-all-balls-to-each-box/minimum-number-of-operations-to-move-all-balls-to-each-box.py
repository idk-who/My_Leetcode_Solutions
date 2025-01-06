class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = [0]*n
        right = [0]*n

        for i in range(1, n):
            left[i] = left[i-1] + (boxes[i-1] == '1')
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + (boxes[i+1] == '1')
        
        for i in range(1, n):
            left[i] += left[i-1]
        
        for i in range(n-2, -1, -1):
            right[i] += right[i+1]
        
        return [i+j for i, j in zip(left, right)]