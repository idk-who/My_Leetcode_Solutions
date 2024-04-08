class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one = 0
        zero = 0
        for i in students:
            if i == 0: zero += 1
            else: one += 1

        for i in sandwiches:
            if i == 0:
                if zero < 1:
                    break
                zero -= 1
            else:
                if one < 1:
                    break
                one -= 1
        
        return one + zero