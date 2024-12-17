class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0]*26
        for i in s:
            freq[ord(i)-ord('a')] += 1
        
        ans = []
        ptr = 26-1
        next_ptr = 26-2

        while ptr >= 0:
            if freq[ptr] == 0:
                ptr -= 1
                continue

            to_use = min(freq[ptr], repeatLimit)
            ans += [chr(ptr+ord('a'))]*to_use
            freq[ptr] -= to_use

            if freq[ptr] > 0:
                while next_ptr >= ptr:
                    next_ptr -= 1
                while next_ptr >= 0 and freq[next_ptr] == 0:
                    next_ptr -= 1
                if next_ptr < 0:
                    break
                ans += [chr(next_ptr+ord('a'))]
                freq[next_ptr] -= 1
        
        return "".join(ans)