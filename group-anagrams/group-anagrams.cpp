class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dict;
        string hash;
        for (auto& s : strs){
            hash = s;
            sort(hash.begin(), hash.end());
            dict[hash].push_back(s);  
        }

        vector<vector<string>> answer;

        for (auto& i : dict){
            answer.push_back(i.second);
        }
        
        return answer;
    }
};
