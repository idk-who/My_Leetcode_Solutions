class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        
        for i in s:
            if i.isalpha():
                st.append(i)
            else:
                st.pop()

        return "".join(st)