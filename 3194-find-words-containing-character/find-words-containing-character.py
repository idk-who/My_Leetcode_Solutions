class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [ind for ind, word in enumerate(words) if x in word]