class Solution
{
public:
    int N;
    vector<vector<string>> answer;
    vector<string> board;

    vector<vector<string>> solveNQueens(int n)
    {
        N = n;
        board = vector<string> (n, string(n,'.'));
        solveNQueensRec();
        return answer;
    }

    void solveNQueensRec(int col = 0)
    {
        if (col == N){
            answer.push_back(board);
            return;
        }

        for (int i = 0; i < N; i++)
        {
            if (isSafe(i, col))
            {
                board[i][col] = 'Q';
                solveNQueensRec(col + 1);
                board[i][col] = '.';
            }
        }
        return;
    }

    bool isSafe(int row, int col)
    {
        for (int i = 0; i < col; i++)
        {
            if (board[row][i] == 'Q')
                return false;
        }

        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        {
            if (board[i][j] == 'Q')
                return false;
        }

        for (int i = row, j = col; i < N && j >= 0; i++, j--)
        {
            if (board[i][j] == 'Q')
                return false;
        }

        return true;
    }
};
