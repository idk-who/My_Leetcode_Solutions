class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()

        for i in arr:
            if 2*i in d or i/2 in d:
                return True
            d.add(i)
        return False