class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_dict = Counter(words)

        n = len(words)
        m = len(words[0])
        k = len(s)
        ans = []

        for i in range(k-n*m+1):
            temp = defaultdict(int)

            for j in range(i, i+n*m, m):
                if s[j:j+m] in word_dict:
                    temp[s[j:j+m]] += 1
                else:
                    break
            
            if temp == word_dict:
                ans.append(i)

        return ans
