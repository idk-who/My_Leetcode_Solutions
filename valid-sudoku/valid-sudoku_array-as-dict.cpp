class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> dict (10, 0);

        for(int i = 0; i < 9; i++){
            for(int j = 0; j<9; j++){
                if (board[i][j] == '.') continue;
                else if  (dict[board[i][j]-48]>0) return false;
                else dict[board[i][j]-48]++;
            }
            dict = vector<int> (10, 0);
        }

        for(int i = 0; i < 9; i++){
            for(int j = 0; j<9; j++){
                if (board[j][i] == '.') continue;
                else if (dict[board[j][i]-48]>0) return false;
                else dict[board[j][i]-48]++;
            }
            dict = vector<int> (10, 0);
        }

        for (int i = 0; i < 9; i+=3){
            for (int j = 0; j < 9; j+=3){
                for (int p = i; p <i+3; p++){
                    for (int q = j; q<j+3;q++){
                        if (board[p][q] == '.') continue;
                        else if (dict[board[p][q]-48]>0) return false;
                        else dict[board[p][q]-48]++;
                    }
                }
            dict = vector<int> (10, 0);
            }
        }

        return true;
    }
};
