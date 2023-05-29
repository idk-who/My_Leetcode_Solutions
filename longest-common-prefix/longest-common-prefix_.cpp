#include <string>

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string out = "";

        int smallest = strs[0].size(); 
        for ( int i = 1; i < strs.size(); i++ ) {
            if ( smallest > strs[i].size() ) {
                smallest = strs[i].size();
            }
        }

        char c;
        for(int n = 0; n < smallest; n++){
            c = strs[0][n]; 
            for(int i = 1; i<strs.size(); i++){
                if (c != strs[i][n]){
                    return out;
                }
            }
            out += c;
        }
        return out;
    }
};
