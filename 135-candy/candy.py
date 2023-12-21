class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        candies = len(ratings)
        valley = 0
        ptr = 1
        while ptr<len(ratings): 

            peak = 0
            while ptr<len(ratings) and ratings[ptr] > ratings[ptr-1]:
                peak += 1
                candies += peak
                ptr += 1
                # print("incr", ptr, peak, valley, candies)

            valley = 0
            while ptr<len(ratings) and ratings[ptr] < ratings[ptr-1]:
                valley += 1
                candies += valley
                ptr += 1
                # print("decr", ptr, peak, valley, candies)

            candies -= min(peak, valley)
            
            while ptr<len(ratings) and ratings[ptr] == ratings[ptr-1]:
                peak = ptr
                valley = ptr
                ptr += 1
                # print("nutr", ptr, peak, valley, candies)
            
        return candies


