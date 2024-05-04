class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        start = 0 
        end = len(people)-1
        ans = 0
        while start<=end:
            if people[start]+people[end] <= limit:
                ans += 1
                end -= 1
            else:
                ans += 1
            start += 1
        
        return ans