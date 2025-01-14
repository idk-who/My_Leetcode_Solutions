class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        temp = [0]*(len(A)+1)
        ans = []
        for i in range(len(A)):
            temp[A[i]] += 1
            temp[B[i]] += 1

            ans.append(sum([1 for i in temp if i == 2]))
        
        return ans