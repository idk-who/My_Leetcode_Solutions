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
        self.helper(digits, 0, [])
        return self.ans

    def helper(self, digits, ptr, carrier):
        if ptr == len(digits):
            self.ans.append("".join(carrier))
            return
        
        # print(ptr, digits)
        for c in self.map[digits[ptr]]:
            carrier.append(c)
            self.helper(digits, ptr+1, carrier)
            carrier.pop()
