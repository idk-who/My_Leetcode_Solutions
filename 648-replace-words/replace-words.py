class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)
        minl = min(map(len, d))
        maxl = min(map(len, d))
        
        ans = []
        
        for word in sentence.split():
            lword = len(word)
            mword = word
            for i in range(min(minl, lword), max(maxl, lword)):
                if word[:i] in d:
                    mword = word[:i]
                    break
            ans.append(mword)

        return " ".join(ans)