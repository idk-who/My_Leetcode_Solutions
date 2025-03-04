class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        num = n
        used = set()
        while num > 0:
            diff = 1
            while diff*3 <= num:
                diff = diff * 3
            if diff in used:
                return False
            used.add(diff)
            num = num - diff
        
        return num == 0