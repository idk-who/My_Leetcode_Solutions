class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        tracker = {0:-1}
        counter = 0
        counter_prev = 0
        
        for i, char in enumerate(s):
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
            else:
                pass
            
            if counter not in tracker or counter_prev < counter:
                tracker[counter] = i
            else:
                max_len = max(max_len, i - tracker[counter])

            counter_prev = counter
        
        return max_len