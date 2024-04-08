class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = [0, 0]
        for i in students: c[i] += 1
        for i in sandwiches:
            if c[i] == 0:
                break
            c[i] -= 1

        return c[0] + c[1]
