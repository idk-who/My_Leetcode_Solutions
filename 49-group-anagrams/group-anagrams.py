class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            d[tuple(sorted(list(word)))].append(word)

        return list(d.values())