class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]
        ans = []
        chars = set(words[0])
        for char in chars:
            count = min([word.count(char) for word in words])
            ans += [char] * count

        return ans
