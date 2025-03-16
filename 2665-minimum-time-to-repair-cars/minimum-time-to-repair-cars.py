class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def poss(minutes):
            repaired = 0

            for r in ranks:
                repaired += (
                    int((minutes/r)**0.5)
                )
                
            return repaired >= cars

        
        mi = 0
        ma = max(ranks)*(cars**2)
        ans = float('inf')

        while mi <= ma:
            mid = (mi+ma)//2
            if poss(mid):
                ans = mid
                ma = mid - 1
            else:
                mi = mid + 1
        
        return ans