class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranks = dict()
        for i in range(len(sorted_score)):
            ranks[sorted_score[i]] = i + 1
        
        ans = [-1]*len(score)

        for i in range(len(score)):
            rank = ranks[score[i]]
            if rank == 1:
                ans[i] = "Gold Medal"
            elif rank == 2:
                ans[i] = "Silver Medal"
            elif rank == 3:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(rank)
        
        return ans