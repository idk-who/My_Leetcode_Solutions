class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size()==0) return 0;
        sort(nums.begin(), nums.end());

        int longest = 0;
        int current = 0;
        for (int i = 0; i<nums.size()-1; i++){
            if (nums[i] == nums[i+1]) continue;
            else if (nums[i]+1==nums[i+1]) current++;
            else current = 0;
            if (current > longest) longest = current;
        }

        return longest+1;
    }
};