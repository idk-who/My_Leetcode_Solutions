class Solution():
    def strangePrinter(self, s):
        cache = dict()

        def solve(s):
            if not s:
                return 0
            if s in cache:
                return cache[s]
            # cost to simply insert last character
            cost = solve(s[0:-1]) + 1
            # what if last character could be inserted for free just by reusing previous step that already prints it?
			# . . . . . A . . . . A
			# |---------| |-----| last character is free
            char_to_insert = s[-1]
            for i, c in enumerate(s[:-1]):
                if c == char_to_insert:
                    cost = min(cost, solve(s[0:i + 1]) + solve(s[i + 1:-1]))
            cache[s] = cost
            return cost

        return solve(s)