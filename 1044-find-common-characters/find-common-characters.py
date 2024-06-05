class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]
        ans = []
        chars = set(words[0])
        for char in chars:
            count = len(words[0])
            for word in words:
                cnt = 0
                for c in word:
                    if c == char: cnt += 1
                count = min(count, cnt)
            ans += [char] * count

        return ans
