class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort()

        vertical = 0
        ma_end = rectangles[0][2]
        for s, _, e, _ in rectangles:
            # print(ma_end, s, e)
            if ma_end <= s:
                vertical += 1
            ma_end = max(ma_end, e)
        
        rectangles.sort(key = lambda x: x[1])
        horizontal = 0
        ma_end = rectangles[0][3]
        for _, s, _, e in rectangles:
            # print(ma_end, s, e)
            if ma_end <= s:
                horizontal += 1
            ma_end = max(ma_end, e)
        print(vertical, horizontal)
        return vertical >= 2 or horizontal >= 2
