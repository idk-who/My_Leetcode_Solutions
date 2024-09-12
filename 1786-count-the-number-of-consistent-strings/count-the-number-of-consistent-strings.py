class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum([1 if all(c in allowed for c in word) else 0 for word in words])