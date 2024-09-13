class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        temp = 0
        
        for i in arr:
            temp ^= i
            pre.append(temp)
        
        ans = []

        for i, j in queries:
            ans.append(pre[i]^pre[j+1])
        
        return ans