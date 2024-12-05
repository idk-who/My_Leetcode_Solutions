class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        p1 = 0
        p2 = 0

        while p1 < n or p2 < n:
            while p1 < n and start[p1] == "_" :
                p1 += 1
            while p2 < n and target[p2] == "_":
                p2 += 1
                
            if p1 == n and p2 == n:
                return True
            if p1 == n or p2 == n:
                return False

            if start[p1] == target[p2]:
                if start[p1] == 'L':
                    if p1 < p2:
                        return False
                else:
                    if p1 > p2:
                        return False
                p1 += 1
                p2 += 1
            else:
                return False

        return True

        