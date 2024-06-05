class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = [len(words[0])]*26

        for word in words:
            new_freq = [0]*26
            for w in word:
                new_freq[ord(w)-ord('a')] += 1
            
            for i in range(26):
                freq[i] = min(freq[i], new_freq[i])

        ans = []
        for i in range(26):
            for _ in range(freq[i]):
                ans.append(chr(i+97))
        
        return ans
