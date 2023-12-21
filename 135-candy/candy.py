class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = len(ratings)
        ptr = 1

        while ptr<len(ratings): 

            peak = 0
            while ptr<len(ratings) and ratings[ptr] > ratings[ptr-1]:
                peak += 1
                candies += peak
                ptr += 1

            valley = 0
            while ptr<len(ratings) and ratings[ptr] < ratings[ptr-1]:
                valley += 1
                candies += valley
                ptr += 1

            candies -= min(peak, valley)
            
            while ptr<len(ratings) and ratings[ptr] == ratings[ptr-1]:
                peak = ptr
                valley = ptr
                ptr += 1
            
        return candies