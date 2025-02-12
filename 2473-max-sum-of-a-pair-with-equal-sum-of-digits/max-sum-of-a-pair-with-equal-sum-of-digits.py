class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)

        for i in nums:
            dig = i
            dig_sum = 0
            while dig:
                dig_sum += dig % 10
                dig //= 10
            d[dig_sum].append(i)
        
        def sum_greatest_two(lst):
            g1 = None
            g2 = None

            for i in lst:
                if g1 is None:
                    g1 = i
                elif i > g1:
                    g2 = g1
                    g1 = i
                elif g2 is None:
                    g2 = i
                elif i > g2:
                    g2 = i
            
            return g1 + g2

        ans = -1
        for k, v in d.items():
            if len(v) >= 2:
                ans = max(
                    ans,
                    sum_greatest_two(v)
                )
        
        return ans