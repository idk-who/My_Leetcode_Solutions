class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        if n < 3 or m < 3: return 0

        desired_freq = [0]+[1]*9

        def is_magic(i, j):
            freq = [0]*10
            d1_sum = 0
            d2_sum = 0
            row_sum = [0]*3
            col_sum = [0]*3

            for k in range(i, i+3):
                for l in range(j, j+3):
                    row_sum[k-i] += grid[k][l]
                    col_sum[l-j] += grid[k][l]
                    if k-i == l-j:
                        d1_sum += grid[k][l]
                    if (k-i + l-j) == 2:
                        d2_sum += grid[k][l]
                    if not (0 <= grid[k][l] <= 9):
                        return False
                    freq[grid[k][l]] += 1
            
            if freq != desired_freq:
                return False
            if d1_sum != d2_sum:
                return False
            for ele in row_sum:
                if d1_sum != ele:
                    return False
            for ele in col_sum:
                if d1_sum != ele:    
                    return False
            
            return True


        ans = 0

        for i in range(n-2):
            for j in range(n-2):
                if is_magic(i, j):
                    ans += 1
                


        
        return ans
                        

                
                
                