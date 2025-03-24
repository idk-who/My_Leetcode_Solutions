class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_days = 0
        day = 1
        ptr = 0
        while day < days+1 and ptr < len(meetings):
            s, e = meetings[ptr][0], meetings[ptr][1]
            if s > day:
                free_days += s-day
            day = max(day, e + 1)
            ptr += 1
            # print(s, e, day, free_days)
        if day < days+1:
            free_days += days-day+1
        
        return free_days

