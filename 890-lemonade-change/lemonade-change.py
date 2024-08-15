class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {
            5:0,
            10:0,
            20:0
        }

        for b in bills:
            notes[b] += 1
            
            rem = b - 5

            if rem >= 10 and notes[10]:
                notes[10] -= 1
                rem -= 10
            if rem:
                num_fives = rem // 5
                if notes[5] >= num_fives:
                    notes[5] -= num_fives
                else:
                    return False

        return True