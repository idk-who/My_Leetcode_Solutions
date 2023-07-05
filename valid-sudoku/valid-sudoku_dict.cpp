class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<char, int> dict;

        for(int i = 0; i < 9; i++){
            for(int j = 0; j<9; j++){
                if (board[i][j] == '.') continue;
                else if  (dict[board[i][j]]>0) return false;
                else dict[board[i][j]]++;
            }
            dict.clear();
        }

        for(int i = 0; i < 9; i++){
            for(int j = 0; j<9; j++){
                if (board[j][i] == '.') continue;
                else if (dict[board[j][i]]>0) return false;
                else dict[board[j][i]]++;
            }
            dict.clear();
        }

        for (int i = 0; i < 9; i+=3){
            for (int j = 0; j < 9; j+=3){
                for (int p = i; p <i+3; p++){
                    for (int q = j; q<j+3;q++){
                        if (board[p][q] == '.') continue;
                        else if (dict[board[p][q]]>0) return false;
                        else dict[board[p][q]]++;
                    }
                }
                dict.clear();
            }
        }

        return true;
    }
};
