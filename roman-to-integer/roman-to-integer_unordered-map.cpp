#include <unordered_map>
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> dict = {
            {'I',1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000}
        };
        int soln = 0;
        for (int i = 0; i < s.size(); i++){
            if(dict[s[i]]<dict[s[i+1]])
                soln -= dict[s[i]];
            else
                soln += dict[s[i]];
        }
        return soln;
    }
};
