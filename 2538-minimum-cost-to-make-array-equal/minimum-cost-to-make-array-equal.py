class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        num_cost = list(zip(nums, cost))
        num_cost.sort(reverse = True)

        num = num_cost[0][0]
        temp_cost = num_cost[0][1]
        cost = 0
        total_cost = 0
        for n, c in num_cost:
            cost += (num-n)*c
            total_cost += c
        total_cost -= temp_cost
        _min = cost

        for i in range(1, len(nums)):
            new_num = num_cost[i][0]
            new_cost = num_cost[i][1]
            cost = cost - (total_cost*(num-new_num)) + (num-new_num)*temp_cost
            _min = min(cost, _min)
            total_cost -= new_cost
            temp_cost += new_cost
            num = new_num
        
        return _min