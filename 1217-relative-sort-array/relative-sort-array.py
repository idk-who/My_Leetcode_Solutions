class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = defaultdict(int)

        for i in arr1:
            freq[i]+=1

        ptr = 0
        for i in arr2:
            while freq[i] > 0:
                arr1[ptr] = i
                freq[i] -= 1
                ptr += 1
            del freq[i]
        
        for i in sorted(freq.keys()):
            while freq[i] > 0:
                arr1[ptr] = i
                freq[i] -= 1
                ptr += 1 
        return arr1