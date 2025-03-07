class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        xor = 0
        for i in range(1, n**2 + 1):
            xor ^= i
        for i in grid:
            for j in i:
                xor ^= j

        one, two = 0, 0
        for i in range(1, n**2 + 1):
            if i & (xor&~(xor-1)):
                one ^= i
            else:
                two ^= i
        for i in grid:
            for j in i:
                if j & (xor&~(xor-1)):
                    one ^= j
                else:
                    two ^= j
            
        for i in grid:
            if one in i:
                return [one, two]
        
        return [two, one]