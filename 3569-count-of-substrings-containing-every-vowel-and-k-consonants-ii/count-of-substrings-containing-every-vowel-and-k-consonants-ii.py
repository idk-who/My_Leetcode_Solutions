class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = {
            'a':-1,
            'e':-1,
            'i':-1,
            'o':-1,
            'u':-1
        }
        consonant_inds = {0:-1}
        consonant_cnt = 0
        ans = 0

        for i in range(n):
            if word[i] in vowels:
                vowels[word[i]] = i
            else:
                consonant_cnt += 1
                consonant_inds[consonant_cnt] = i
            
            if (consonant_cnt - k in consonant_inds and
                all([i!=-1 for i in vowels.values()]) and
                consonant_inds[consonant_cnt - k] < min(vowels.values())
                ):
                ans += (
                    min(
                        *vowels.values(),
                        consonant_inds[consonant_cnt - k + 1] if consonant_cnt - k + 1 in consonant_inds else float('inf')
                    ) - 
                    consonant_inds[consonant_cnt - k]
                )
                # print(ans, i, vowels, consonant_inds)
        return ans

        