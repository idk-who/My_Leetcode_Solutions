class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        mapping = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        def rec(digits, ptr, temp, ans):
            if ptr == len(digits):
                ans.append(temp)
                return
            for c in mapping[int(digits[ptr])]:
                rec(digits, ptr+1, temp+c, ans)

        ans = []
        rec(digits, 0, "", ans)
        return ans