class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        m = len(words[0])
        k = len(s)
        ans = []
        word_dict = defaultdict(int)
        for w in words:
            word_dict[w] += 1
        for i in range(k):
            temp = word_dict.copy()

            j = i
            while j+m<=k and temp[s[j:j+m]]>0:
                temp[s[j:j+m]] -= 1
                j += m
            
            for v in temp.values():
                if v > 0:
                    break
            else:
                ans.append(i)

        return ans