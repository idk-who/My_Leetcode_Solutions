class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        ma = 0
        mi = 0

        curr = 0
        for i in differences:
            curr += i
            mi = min(mi, curr)
            ma = max(ma, curr)
        
        return max(0, (upper-lower)-(ma-mi)+1)