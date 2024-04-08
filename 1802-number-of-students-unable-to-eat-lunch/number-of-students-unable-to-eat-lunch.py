class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)

        for i in sandwiches:
            if i == 0:
                if c[0] < 1:
                    break
                c[0] -= 1
            else:
                if c[1] < 1:
                    break
                c[1] -= 1
        
        return c[0] + c[1]