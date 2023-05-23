class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> dict;

        for(int i = 0; i<nums.size(); i++){
            if(dict.count(nums[i])==1) return true;
            else dict[nums[i]] = true;
        }
        return false;
    }
};