class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = 0
        cnt = 1

        for i in range(1, n):
            if colors[i] != colors[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans += 1
        
        for i in range(k-1):
            if colors[i] != colors[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans += 1
                
        return ans



