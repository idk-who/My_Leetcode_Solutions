class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        ptr = 0
        while ptr<k:
            temp = happiness[ptr]-ptr
            if temp <= 0: break 
            ans += temp
            ptr += 1
        
        return ans