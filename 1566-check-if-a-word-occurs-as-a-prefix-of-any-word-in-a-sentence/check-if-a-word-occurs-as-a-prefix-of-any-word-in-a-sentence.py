class Solution:
    def isPrefixOfWord(self, sent: str, sw: str) -> int:
        for ind, i in enumerate(sent.split()):
            if i.startswith(sw):
                return ind + 1
        return -1