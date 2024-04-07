class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []
        for ind, i in enumerate(s):
            if i == "*":
                s2.append(ind)
            elif i == "(":
                s1.append(ind)
            else:
                if len(s1)!=0:
                    s1.pop()
                elif len(s2)!=0:
                    s2.pop()
                else:
                    return False
            
        while len(s1)!=0 and len(s2)!=0:
            if s1.pop()>s2.pop(): return False
        
        return len(s1)==0
                 
        
