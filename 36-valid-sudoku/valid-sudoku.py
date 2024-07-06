class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = [False]*10
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != '.':
                            if s[int(board[k][l])]:
                                return False
                            s[int(board[k][l])] = True
        for i in range(9):
            s = [False]*10
            for j in range(9):
                if board[i][j] != '.':
                    if s[int(board[i][j])]:
                        return False
                    s[int(board[i][j])] = True

        for i in range(9):
            s = [False]*10
            for j in range(9):
                if board[j][i] != '.':
                    if s[int(board[j][i])]:
                        return False
                    s[int(board[j][i])] = True
        
        return True