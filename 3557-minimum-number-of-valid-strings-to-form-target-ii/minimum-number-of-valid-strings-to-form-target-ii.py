class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        dp = [0] * len(target)

        def search(prefix):
            for word in words:
                if word.startswith(prefix): return True
            return False 

        left, right = 0, 0
        
        for i in range(len(target)):
            while not search(target[left:right + 1]) and left <= right: left += 1
            
            if left > right: return -1

            substrLen = right - left + 1
            dp[i] = 1 if i < substrLen else dp[i - substrLen] + 1

            right += 1

        return dp[-1]