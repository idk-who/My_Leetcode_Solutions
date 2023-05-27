class Solution {
public:
    bool isPalindrome(string s) {

        auto p1 = 0;
        auto p2 = s.size() - 1;
        while(p2>p1){
            if (!iswalnum(s[p1])){
                p1++;
                continue;
            }
            if (!iswalnum(s[p2])){
                p2--;
                continue;
            }
            if (!(tolower(s[p1]) == tolower(s[p2]))){
                return false;
            }
            p1++;
            p2--;
        }
        return true;
    }
};