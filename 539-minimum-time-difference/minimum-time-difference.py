class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def diff(t1, t2):
            return min(
                ((int(t1[:2])*60 + int(t1[3:])) - 
                (int(t2[:2])*60 + int(t2[3:]))),
                1440 - 
                ((int(t1[:2])*60 + int(t1[3:])) - 
                (int(t2[:2])*60 + int(t2[3:])))
            )

        ans = float("inf")
        for i in range(1, len(timePoints)):
            ans = min(
                ans,
                diff(timePoints[i], timePoints[i-1])
            )
        ans = min(
            ans,
            diff(timePoints[-1], timePoints[0])
        )
        
        return ans