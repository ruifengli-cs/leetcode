class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return ''
        opened = 0
        res = []
        for ch in S:
            if ch == '(' and opened > 0:
                res.append(ch)
            if ch == ')' and opened > 1:
                res.append(ch)
            opened += 1 if ch == '(' else -1
        return "".join(res)