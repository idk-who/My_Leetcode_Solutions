from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        ans = deque()
        for i in deck:
            ans.rotate()
            ans.appendleft(i)
        
        return list(ans)