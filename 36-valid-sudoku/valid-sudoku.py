class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] in s:
                            return False
                        if board[k][l] != '.':
                            s.add(board[k][l])
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                if board[i][j] != ".":
                    s.add(board[i][j])
                    
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                if board[j][i] != ".":
                    s.add(board[j][i])
        
        return True