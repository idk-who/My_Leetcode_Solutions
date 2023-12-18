class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2: return 1
        dic = {}
        candies = [0]*len(ratings)
        for i in range(len(ratings)):
            if ratings[i] in dic:
                dic[ratings[i]].append(i)
            else:
                dic[ratings[i]] = [i]

        # print(dic)
        for r, inds in sorted(dic.items()):
            # print(r, inds)
            temp = candies[:]
            for i in inds:
                if i==0:
                    candies[i] = temp[i+1]+1
                elif i==len(ratings)-1:
                    candies[i] = temp[i-1]+1
                else:
                    candies[i] = max(temp[i-1], temp[i+1])+1 

        return sum(candies)

