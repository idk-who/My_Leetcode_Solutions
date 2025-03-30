class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = [0]*26
        for i in s:
            freq[ord(i)-ord('a')] += 1
        
        chars = set()
        cnt_zero = 0
        le = 0
        ans = []

        for i in s:
            chars.add(i)
            freq[ord(i)-ord('a')] -= 1
            if freq[ord(i)-ord('a')] == 0:
                cnt_zero += 1
            le += 1
            
            if cnt_zero == len(chars):
                ans.append(le)
                le = 0
                chars = set()
                cnt_zero = 0
        
        return ans