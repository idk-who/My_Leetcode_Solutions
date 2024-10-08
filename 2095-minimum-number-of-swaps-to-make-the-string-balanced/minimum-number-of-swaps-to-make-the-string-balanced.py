class Solution:
    def minSwaps(self, s: str) -> int:
        mismatched = 0
        left_par = 0

        for i in s:
            if i == '[':
                left_par += 1
            else:
                if left_par:
                    left_par -= 1
                else:
                    mismatched += 1
        
        return mismatched // 2 + (mismatched & 1)