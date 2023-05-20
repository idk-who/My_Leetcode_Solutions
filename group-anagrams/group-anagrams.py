class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def prime_hash(str):
            prime_factors = [
                2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                31, 37, 41, 43, 47, 53, 59, 61, 67, 
                71, 73, 79, 83, 89, 97, 101
            ] 
            hash = 1
            for i in str:
                hash *= prime_factors[(ord(i) - 97)]
            
            return hash

        hashes = []
        for i in strs:
            hashes.append(prime_hash(i))
        
        coupled = [(i,j) for i,j in zip(hashes, strs)]

        coupled = sorted(coupled, key=lambda x: x[0])

        answer = []

        temp = [coupled[0]]
        n = 0 
        for i in coupled[1:]:
            if i[0] == temp[0][0]:
                temp.append(i)
            else:
                answer.append(temp)
                temp = [i]
        answer.append(temp)
        
        answer = [[j[1] for j in i] for i in answer]

        return answer