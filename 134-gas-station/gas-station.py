class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        end  = 0
        n = len(gas)

        while start<n:
            tank+=gas[end%n]
            if end%n == start and end>start:
                return start
            elif tank>=cost[end%n]:
                tank-=cost[end%n]
            else:
                start = end + 1
                tank = 0
            end+=1
        
        return -1
        

            