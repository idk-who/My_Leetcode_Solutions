class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n, m = len(grid), len(grid[0])
        mod = grid[0][0] % x

        nums = defaultdict(int)

        for i in range(n):
            for j in range(m):
                if grid[i][j] % x != mod:
                    return -1
                nums[grid[i][j]] += 1
        
        ops = sum([(k//x)*f for k, f in nums.items()])
        ans = ops
        val = mod
        left = 0
        right = sum([f for f in nums.values()])
        # print(ops)
        for k, f in sorted(nums.items()):
            # print(k, f, ops)
            ops -= ((k-val)//x)*right
            ops += ((k-val)//x)*left
            left += f
            right -= f
            val = k
            # print(left, right)

            ans = min(ans, ops)
        
        return ans