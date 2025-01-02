class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        pre_sum = [0]
        su = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                su += 1
            pre_sum.append(su)
        
        ans = []
        for l, r in queries:
            ans.append(pre_sum[r+1] - pre_sum[l])
        
        return ans
