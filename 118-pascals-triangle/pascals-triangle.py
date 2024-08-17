class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(1, numRows):
            triangle.append(
                list(map(
                    lambda x, y: x+y, 
                    [0]+triangle[-1], 
                    triangle[-1]+[0]
                    ))
                )
        
        return triangle
            

