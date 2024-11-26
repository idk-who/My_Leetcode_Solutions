class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = [0]*n
        for u, v in edges:
            teams[v] += 1
        if teams.count(0) > 1: 
            return -1
        return teams.index(0)