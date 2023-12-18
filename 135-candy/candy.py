class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
         0 = greater than no one
         1 = greater than left
         2 = greater than right 
         3 = greater than left and right 
        """
        diff = [0]*len(ratings)
        for i in range(len(ratings)):
            if i != len(ratings)-1 and ratings[i]>ratings[i+1]:
                diff[i]+=2
            if i != 0 and ratings[i]>ratings[i-1]:
                diff[i]+=1

        candies = [0]*len(ratings)
        for i in range(len(ratings)):
            if diff[i] == 0:
                candies[i]=1
            elif diff[i] == 1:
                candies[i] = candies[i-1]+1
        for i in range(len(ratings)-1, -1, -1):
            if diff[i] == 2:
                candies[i] = candies[i+1]+1
            elif diff[i] == 3:
                candies[i] = max(candies[i-1], candies[i+1]) + 1
            
        return sum(candies)

