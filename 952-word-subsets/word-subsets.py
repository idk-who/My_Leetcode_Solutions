class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # max char requirements
        max_req = [0]*26

        for w in words2:
            freq = [0]*26
            for c in w:
                freq[ord(c)-ord('a')] += 1
            
            for i in range(26):
                max_req[i] = max(
                    max_req[i],
                    freq[i]
                )
        
        ans = []
        for w in words1:
            freq = [0]*26
            for c in w:
                freq[ord(c)-ord('a')] += 1
            
            # is universal
            is_uni = True

            for i in range(26):
                if max_req[i] > freq[i]:
                    is_uni = False
                    break
            
            if is_uni:
                ans.append(w)
        
        return ans