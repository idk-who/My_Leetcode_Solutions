class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (auto& i : nums){
            freq[i]++;
        }

        vector<int> answer;
        pair<int, int> greatest; 
        for (int i = 0; i < k; i++){
            greatest.first = INT_MIN;
            greatest.second = INT_MIN;
            for (auto& p : freq){
                if (p.second > greatest.second)
                    greatest = p;
            }
            answer.push_back(greatest.first);
            freq.erase(greatest.first);
        }

        return answer;
    }
};