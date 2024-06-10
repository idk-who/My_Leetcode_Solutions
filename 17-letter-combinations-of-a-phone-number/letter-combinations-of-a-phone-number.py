class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.ans = []
        self.map = [
            '',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]
        digits = list(map(int, list(digits)))
        # print(digits)
        self.helper(digits, 0, "")
        return self.ans

    def helper(self, digits, ptr, carrier):
        if ptr == len(digits):
            self.ans.append(carrier)
            return
        
        # print(ptr, digits)
        for c in self.map[digits[ptr]]:
            self.helper(digits, ptr+1, carrier+c)
