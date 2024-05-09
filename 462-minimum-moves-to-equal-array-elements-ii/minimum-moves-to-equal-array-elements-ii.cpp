class Solution {
public:
    int minMoves2(vector<int>& nums) {

        //sort the array 
        sort(nums.begin(),nums.end());


        int n=nums.size();

        //each element of array should be nums[n/2] then only we reduce the number of moves
        int ans=nums[n/2];
        int sum=0;
        for(auto ele:nums){
            sum+=abs(ele-ans);//just count the absolute difference of each element of nums
        }

        return sum;//return sum
    }
};