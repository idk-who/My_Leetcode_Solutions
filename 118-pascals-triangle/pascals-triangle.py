class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(numRows-1):
            row = [1]
            for j in range(i):
                row.append(triangle[-1][j]+triangle[-1][j+1])
            row.append(1)
        
            triangle.append(row)
        
        return triangle
            
