class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer(nums.size(), 1);
        int temp1 = 1;
        int temp2 = 1;
        int n = nums.size() - 2;
        for (int i = 1; i<nums.size(); i++){
            temp1 *= nums[i-1];
            answer[i] *= temp1;
            temp2 *= nums[n+1];
            answer[n] *= temp2;
            n--;
        }
        return answer;
    }
};