class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        representation = []
        while n:
            representation.append(n%3)
            n //= 3
        print(representation[::-1])
            
        
        return all([i!= 2 for i in representation])