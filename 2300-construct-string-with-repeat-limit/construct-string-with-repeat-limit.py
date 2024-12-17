class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0]*26
        for i in s:
            freq[ord(i)-ord('a')] += 1
        
        ans = []
        ptr = 26-1

        while ptr >= 0:
            if freq[ptr] == 0:
                ptr -= 1
                continue

            to_use = min(freq[ptr], repeatLimit)
            ans += [chr(ptr+ord('a'))]*to_use
            freq[ptr] -= to_use

            if freq[ptr] > 0:
                next_chr = ptr - 1
                while next_chr >= 0 and freq[next_chr] == 0:
                    next_chr -= 1
                if next_chr < 0:
                    break
                ans += [chr(next_chr+ord('a'))]
                freq[next_chr] -= 1
            else:
                ptr -= 1
        
        return "".join(ans)