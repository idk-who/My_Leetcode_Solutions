class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            m = l + (r-l)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        
        row = m

        l = 0
        r = len(matrix[0])-1

        while l <= r:
            m = l + (r-l)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
