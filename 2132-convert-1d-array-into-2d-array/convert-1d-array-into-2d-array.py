class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n: return []
        ans = []
        for i in range(0, m*n, n):
            ans.append(original[i:i+n])
        return ans