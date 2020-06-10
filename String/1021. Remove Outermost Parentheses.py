class Solution:
    # APP1: count open_left
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return ""
        open_left = 0
        n, res = len(S), []
        for i in range(n):
            if S[i] == '(':
                if open_left > 0:
                    res.append('(')
                open_left += 1
            if S[i] == ')':
                if open_left > 1:
                    res.append(')')
                open_left -= 1
        return ''.join(res)

    # APP2: concise version of APP1:
    def removeOuterParentheses(self, S: str) -> str:
        res, open_left = [], 0
        for ch in S:
            if ch == '(' and open_left > 0:
                res.append(ch)
            if ch == ')' and open_left > 1:
                res.append(ch)
            open_left += 1 if ch == '(' else -1
        return ''.join(res)

    # APP3: two pointers, append string without outer () when open_left == 0
    def removeOuterParentheses(self, S: str) -> str:
        res, open_left, l = [], 0, 0
        for r in range(len(S)):
            if S[r] == '(':
                open_left += 1
            if S[r] == ')':
                open_left -= 1
            if open_left == 0:
                res.append(S[l + 1: r])
                l = r + 1
        return ''.join(res)





