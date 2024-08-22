class Solution:
    def bitwiseComplement(self, num: int) -> int:
        i = 1 
        while i <= num:
            i <<= 1
        return num ^ (i-1) if num != 0 else 1