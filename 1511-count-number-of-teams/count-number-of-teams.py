class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for i, ele in enumerate(rating):
            left_less = left_great = right_less = right_great = 0

            for j in range(0, i):
                if rating[j]<ele:
                    left_less += 1
                else:
                    left_great += 1
            
            for j in range(i+1, n):
                if rating[j]<ele:
                    right_less += 1
                else:
                    right_great += 1
            
            ans += (left_less * right_great)
            ans += (left_great * right_less)
        
        return ans