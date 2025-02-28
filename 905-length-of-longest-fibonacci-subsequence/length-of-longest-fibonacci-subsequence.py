class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        ele_to_index = {arr[i]:i for i in range(n)}
        
        dp = [[0]*n for _ in range(n)]
        ma = 0

        for i in range(n):
            for j in range(i):
                if arr[i]-arr[j] < arr[j] and arr[i]-arr[j] in ele_to_index:
                    prev_idx = ele_to_index[arr[i]-arr[j]]
                    dp[j][i] = dp[prev_idx][j] + 1
                else:
                    dp[j][i] = 2
                ma = max(ma, dp[j][i])

        return ma if ma > 2 else 0

            
            