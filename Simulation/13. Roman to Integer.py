class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        combs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        cur, n, res = 0, len(s), 0
        while cur < n:
            if cur + 1 < n and s[cur: cur + 2] in combs:
                res += combs[s[cur: cur + 2]]
                cur += 2
            else:
                res += symbols[s[cur: cur + 1]]
                cur += 1
        return res