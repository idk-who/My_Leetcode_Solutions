class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = -1
        area = -1

        for l, w in dimensions:
            if (l**2+w**2) > diag:
                diag = (l**2+w**2)
                area = l*w
            elif (l**2+w**2) == diag:
                area = max(area, l*w)
        
        return area