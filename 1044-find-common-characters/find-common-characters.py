class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        chars = set(words[0])
        for char in chars:
            count = float("inf")
            for word in words:
                cnt = 0
                for c in word:
                    if c == char: cnt += 1
                count = min(count, cnt)
            ans += [char] * count

        return ans
