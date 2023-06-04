#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> dict;

        for(int i = 0; i<nums.size(); i++){
            if(dict.count(target-nums[i])){
                return {i, dict.at(target-nums[i])};
            }
            else{
                dict[nums[i]] = i;
            }
        }
    return {};
    }
};
