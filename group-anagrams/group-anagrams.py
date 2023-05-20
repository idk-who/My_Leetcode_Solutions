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
        
        d = {}

        for i in strs:
            key = prime_hash(i)
            if key in d:
                d[key].append(i)
            else:
                d[key] = [i]

        return [i for i in d.values()]

