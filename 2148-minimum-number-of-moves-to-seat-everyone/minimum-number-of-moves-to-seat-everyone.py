class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        freq = [0]*101
        n = len(seats)

        for a, b in zip(seats, students):
            freq[a]+=1
            freq[b]-=1
        
        ans = 0
        for i in range(1,101):
            freq[i] += freq[i-1]
            ans += abs(freq[i])
        
        return ans