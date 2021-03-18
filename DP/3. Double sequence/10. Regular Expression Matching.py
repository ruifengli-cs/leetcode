class Solution:
    # APP1: dfs. first match when s[i] in (p[j], ".")
    # second match
    #     when p[j + 1] == "*", then we can match dfs(i + 1, j) or dfs(i, j + 2)
    #     else return first_match and dfs(i + 1, j + 1)
    # Time: o(2^n) space: O(n^2) Runtime: 12%
    # corner case:
    # 1. aa, a
    # 2. aaa, a*
    # 3. aaa, a*a
    # 4. abc, a..
    # 5. abc, a.*
    # 6. abcddd, a.* d
    # 7. abcddd, a.*c
    # 8. None, a*: cover in dfs
    # 9. ab, None:
    # 10. None, None
    #     def isMatch(self, s: str, p: str) -> bool:
    #         return self.dfs(s, p, 0, 0)

    #     def dfs(self, s, p, i, j):
    #         if j == len(p):
    #             return i >= len(s)
    #         first_match = i < len(s) and p[j] in {s[i], '.'}

    #         if j + 1 < len(p) and p[j + 1] == "*":
    #             return (first_match and self.dfs(s, p, i + 1, j)) or self.dfs(s, p, i, j + 2)
    #         else:
    #             return first_match and self.dfs(s, p, i + 1, j + 1)

    # APP2: dfs + memoization.
    # Time: O(n^2) space: O(n^2) Runtime: 96%
    #     def isMatch(self, s: str, p: str) -> bool:
    #         memo = {}
    #         return self.dfs(s, p, 0, 0, memo)

    #     def dfs(self, s, p, i, j, memo):
    #         if j == len(p):
    #             return i >= len(s)
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #         first_match = i < len(s) and p[j] in {s[i], '.'}
    #         if j + 1 < len(p) and p[j + 1] == '*':
    #             memo[(i, j)] = first_match and self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 2, memo)
    #         else:
    #             memo[(i, j)] = first_match and self.dfs(s, p, i + 1, j + 1, memo)
    #         return memo[(i, j)]

    # APP3: DP. like LCS. f[i][j]: if s[i:] match p[j:]. ans: f[0][0]
    # To calculate f[i][j]:
    #     if p[j] in {s[i], '.'}: first_match = True
    #     if j + 1 < len(p) and p[j + 1] == '*':
    #         f[i][j]  = first_match and f[i + 1][j] or f[i, j + 2]
    #     else:
    #         f[i][j] = first_match and f[i + 1][j + 1]
    # Time: O(n^2) space: O(n^2)
    #     def isMatch(self, s: str, p: str) -> bool:
    #         if not p:
    #             return not s
    #         m, n = len(s), len(p)
    #         f = [[0] * (n + 1) for _ in range(m + 1)]
    #         f[-1][-1] = 1
    #         for i in range(m, -1, -1):
    #             for j in range(n - 1, -1, -1):
    #                 first_match = i < len(s) and p[j] in {s[i], '.'}
    #                 if j + 1 < len(p) and p[j + 1] == '*':
    #                     f[i][j]  = (first_match and f[i + 1][j]) or f[i][j + 2]
    #                 else:
    #                     f[i][j] = first_match and f[i + 1][j + 1]
    #         return f[0][0]

    #     APP4: DP. f[i][j]: if s[:i] match p[:j]. ans: f[m][n]. f[0][0] = 1
    #         if p[j] in {s[i], '.'}: first_match == True
    #         if p[j] == '*':
    #             f[i][j]  = first_match and f[i - 1][j - 1] or f[i][j - 2]
    #         else:
    #             f[i][j] = first_match and f[i - 1][j - 1]

    # APP4. dp like lcs. f[i][j]: if s[:i] match p[:j].
    # if p[j] in [s[i], '.']:
    #     f[i][j] = f[i - 1][j - 1]
    # if p[j] == '*'
    # f[i][j] = (f[i][j - 1] and s[i] match p[j - 1]) or f[i][j - 2]
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        m, n = len(s), len(p)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        self.init(f, p)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in [s[i - 1], '.']:
                    f[i][j] = f[i - 1][j - 1]
                elif j > 1 and p[j - 1] == '*':
                    f[i][j] = (p[j - 2] in [s[i - 1], '.'] and f[i - 1][j]) or f[i][j - 2]
        return f[m][n]

    def init(self, f, p):
        f[0][0] = 1
        p_index = 0
        while p_index < len(p):
            if p_index + 1 >= len(p) or p[p_index + 1] != '*':
                return
            f[0][p_index + 2] = 1
            p_index += 2







