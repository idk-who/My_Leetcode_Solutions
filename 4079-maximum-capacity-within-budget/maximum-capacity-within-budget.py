class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        cst_cap = list(sorted(zip(costs, capacity)))
        cst_sorted = []
        cap_sorted = []
        for i, j in cst_cap:
            cst_sorted.append(i)
            cap_sorted.append(j)
        
        cap_prefix = [cap_sorted[0]]
        for i in range(1, n):
            cap_prefix.append(max(cap_prefix[i-1], cap_sorted[i]))
        
        ans = 0
        # ind = bisect_left(cst_sorted, budget)-1
        # if ind >= 0:
        #     ans = cap_prefix[ind]
        
        j = n-1
        for i in range(n):
            cst = cst_sorted[i]
            if cst >= budget:
                break
            ans = max(
                ans,
                cap_prefix[i]
            )
            rem_budget = budget - cst
            while j >= 0 and cst_sorted[j] >= rem_budget:
                j -= 1
            j2 = min(j, i-1)

            if j2 >= 0:
                ans = max(ans, cap_sorted[i] + cap_prefix[j2])
        
        return ans 