class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> freq (95, 0);
        int max_count = 0;

        int start = 0;
        int end = 0;
        int size = s.size();
        while (start < size && end < size){
            if ((end == size) || freq[s[end]-' ']){
                if (end-start > max_count) max_count = end-start;
                for(int i = start; i < end; i++) freq[s[i]-' '] = 0;
                start ++;
                end = start;
            }

            freq[s[end]-' '] = 1;
            end ++;
        }

        if (end-start > max_count) max_count = end-start;

        return max_count;
    }
};