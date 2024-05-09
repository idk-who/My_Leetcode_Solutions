class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        ptr = 0
        while ptr<k:
            ans += max(happiness[ptr]-ptr, 0)
            ptr += 1
        
        return ans
