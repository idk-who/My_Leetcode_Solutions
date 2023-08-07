class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = m*n - 1

        while(low<=high):
            mid = (high-low) // 2 + low
            index_ele = matrix[mid//n][mid%n]
            if index_ele == target:
                return True
            elif index_ele < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
