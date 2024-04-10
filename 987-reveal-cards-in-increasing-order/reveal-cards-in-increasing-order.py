from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        ans = deque()
        for i in deck:
            if len(ans) > 1:
                ans.append(ans.popleft())
            ans.append(i)
        
        return list(ans)[::-1]