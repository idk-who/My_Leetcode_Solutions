class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = [0]*(len(A)+1)
        ans = []
        cnt = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                cnt += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                cnt += 1

            ans.append(cnt)
        
        return ans