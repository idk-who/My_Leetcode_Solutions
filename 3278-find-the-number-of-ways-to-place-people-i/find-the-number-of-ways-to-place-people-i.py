class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x: (-x[1], x[0]))
        # print(points)
        ans = 0
        for i in range(n):
            x_ma, y_mi = float('inf'), float('-inf')
            for j in range(i+1, n):
                if points[j][0] < points[i][0]:
                    continue
                if points[j][0] < x_ma or points[j][1] > y_mi:
                    ans += 1
                    x_ma = min(x_ma, points[j][0])
                    y_mi = max(y_mi, points[j][1])
        
        return ans
