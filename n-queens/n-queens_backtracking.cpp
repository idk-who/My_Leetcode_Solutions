class Solution
{
public:
    int N;
    vector<vector<string>> answer;
    vector<vector<bool>> board;

    vector<vector<string>> solveNQueens(int n)
    {
        N = n;
        board = vector<vector<bool>>(n, vector<bool>(n, false));
        solveNQueensRec();
        return answer;
    }

    void solveNQueensRec(int col = 0)
    {
        if (col == N){
            append_answer();
            return;
        }

        for (int i = 0; i < N; i++)
        {
            if (isSafe(i, col))
            {
                board[i][col] = 1;
                solveNQueensRec(col + 1);
                board[i][col] = 0;
            }
        }
        return;
    }

    void append_answer()
    {
        answer.push_back({});
        stringstream ss;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (board[i][j])
                {
                    ss << 'Q';
                }
                else
                {
                    ss << '.';
                }
            }
            answer[answer.size()-1].push_back(ss.str());
            ss=stringstream();
        }
        
    }

    bool isSafe(int row, int col)
    {
        for (int i = 0; i < col; i++)
        {
            if (board[row][i])
                return false;
        }

        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        {
            if (board[i][j])
                return false;
        }

        for (int i = row, j = col; i < N && j >= 0; i++, j--)
        {
            if (board[i][j])
                return false;
        }

        return true;
    }
};
