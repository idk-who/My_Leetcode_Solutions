class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
         0 = greater than no one
         -1 = greater than left
         -2 = greater than right 
         -3 = greater than left and right 
        """
        candies = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                candies[i] = max(candies[i+1]+1, candies[i])
            
        return sum(candies)

