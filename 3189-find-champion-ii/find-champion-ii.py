class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = [True]*n
        for u, v in edges:
            teams[v] = False
        if teams.count(True) > 1: 
            return -1
        return teams.index(True)