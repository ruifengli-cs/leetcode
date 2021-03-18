# APP1: dfs: return decode ways for first ith char
# return dfs(i - 1)| s[i] can be decoded + dfs(i - 2)|s[i - 1: i + 1] can be decoded
# Time: O(2^n) space: O(n)

# APP2: dfs + memoizaiton
# TIme: O(n^2) space: O(n)


# APP3: DP
# 1. def: f[i]: decode ways for first ith char
# 2. f[i] = f[i - 1]|s[i] + f[i - 2]|s[i - 1:i + 1]
# 3. ans: f[n]
# 4. init: f[0] = 1
# # Time: O(n^2) space: O(n) -> O(1) runtime: 83%
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return
        n = len(s)
        f = [1] + [0] * n
        single, double_first, double_second = set(['1', '2', '3', '4', '5', '6', '7', '8', '9']), set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']), set(['0', '1', '2', '3', '4', '5', '6'])
        for i in range(1, n + 1):
            if s[i - 1] in single:
                f[i] += f[i - 1]
            if i - 2 >= 0 and ((s[i - 2] == '1' and s[i - 1] in double_first) or (s[i - 2] == '2' and s[i - 1] in double_second)):
                f[i] += f[i - 2]
        return f[n]

# APP4: DP: use one viarable to optimize
# Time: O(n^2) space: O(1) runtime: 83%
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return
        n = len(s)
        pre = prepre = 1
        single, double_first, double_second = set(['1', '2', '3', '4', '5', '6', '7', '8', '9']), set(
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']), set(['0', '1', '2', '3', '4', '5', '6'])
        cur = 0
        for i in range(n):
            cur = 0
            if s[i] in single:
                cur += pre
            if i - 1 >= 0 and (
                    (s[i - 1] == '1' and s[i] in double_first) or (s[i - 1] == '2' and s[i] in double_second)):
                cur += prepre
            pre, prepre = cur, pre
        return cur
