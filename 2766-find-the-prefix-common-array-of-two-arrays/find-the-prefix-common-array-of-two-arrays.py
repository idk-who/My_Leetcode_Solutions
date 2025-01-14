class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = set()
        ans = []
        cnt = 0
        for i in range(len(A)):
            if A[i] in freq:
                cnt += 1
            else:
                freq.add(A[i])
            if B[i] in freq:
                cnt += 1
            else:
                freq.add(B[i])

            ans.append(cnt)
        
        return ans


