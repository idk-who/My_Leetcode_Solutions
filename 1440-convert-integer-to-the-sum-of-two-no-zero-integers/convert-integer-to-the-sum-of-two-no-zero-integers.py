class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        one, two = 1, n-1

        while ('0' in str(one)) or ('0' in str(two)):
            one += 1
            two -= 1
        
        return [one, two]