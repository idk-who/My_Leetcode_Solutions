class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(1, numRows):
            new_row = [1]
            for i in range(i-1):
                new_row.append(ans[-1][i]+ans[-1][i+1])
            new_row.append(1)
            ans.append(new_row)

        return ans
            
