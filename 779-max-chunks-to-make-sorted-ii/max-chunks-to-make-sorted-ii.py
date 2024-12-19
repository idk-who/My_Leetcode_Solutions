class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = []
        d = defaultdict(int)
        for i in arr:
            d[i] += 1
            count.append((i, d[i]))

        chunks = 0
        ma = (0, 0)
        for x, y in zip(count, sorted(count)):
            ma = max(ma, x)
            if y == ma:
                chunks += 1
        
        return chunks


        