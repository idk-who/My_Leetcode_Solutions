class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        
        st = [-1]
        ans = 0
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                
                if st:
                    ans = max(ans, i - st[-1])
                else:
                    st.append(i)
                    
        return ans