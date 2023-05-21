class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dict;
        string hash;
        for (int i=0; i<strs.size(); i++){
            hash = strs[i];
            sort(hash.begin(), hash.end());
            dict[hash].push_back(strs[i]);  
        }

        vector<vector<string>> answer;

        for (auto& i : dict){
            answer.push_back(i.second);
        }
        
        return answer;
    }
};
