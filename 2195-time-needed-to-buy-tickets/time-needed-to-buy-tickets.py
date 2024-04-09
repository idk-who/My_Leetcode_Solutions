class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        nk = tickets[k]
        for i in range(len(tickets)):
            if i < k:
                time += min(nk, tickets[i])
            elif i == k:
                time += nk
            else:
                time += min(nk-1, tickets[i])
            
        return time