class Solution:
    def minAnagramLength(self, s: str) -> int:
        stringList = list(s)
        n = len(s)
        ans = n
        for size in range(1, n):
            if n % size == 0: 
                count = Counter(stringList[:size])

                for j in range(size, n, size):
                    temp = Counter(stringList[j:j+size])

                    if count != temp:
                        break
                else:
                    return size
                    
        return ans