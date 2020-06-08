class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ' ' and s[i - 1] != ' ':
                res += 1
            if i == n - 1 and s[i] != ' ':
                res += 1
        return res