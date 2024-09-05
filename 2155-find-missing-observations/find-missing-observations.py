class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        curSum=sum(rolls)
        obv=n+len(rolls)
        missSum=mean*obv-curSum
        if missSum>6*n or missSum<0 or missSum<n:
            return []
        x=missSum//n
        res=[x]*n
        remain=missSum-x*n
        if remain>0:
            more=6-x
            add=remain//more
            res=res[add:]+[6]*add
            final=remain%more
            res[0]+=final
        return res
        