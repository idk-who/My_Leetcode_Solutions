class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dict;
        string hash;
        for (auto& s : strs){
            dict[optimised_sort(s)].push_back(s);  
        }

        vector<vector<string>> answer;

        for (auto& i : dict){
            answer.push_back(i.second);
        }

        return answer;
    }

    string optimised_sort(string s){
        int freq[26] = {0};
        for (auto& c:s){
            freq[c -'a']++;
        }
        string sorted;
        for (int i = 0; i < 26; i++){
            sorted += string(freq[i], i + 'a');
        }
        return sorted;
    }
};
