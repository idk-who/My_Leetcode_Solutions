class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left_max = values[0]
        ans = 0

        for i in range(1, len(values)):
            ans = max(
                ans,
                values[i]+(left_max-1)
            ) 
            left_max = max(
                left_max - 1,
                values[i]
            )
        
        return ans