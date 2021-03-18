# APP1: DFS + memoization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(2000)
        def dfs(i, j):
            if j == n:
                return i == m
            if i > m:
                return False
            first_match = i < m and p[j] in [s[i], "."]
            if j + 1 < n and p[j + 1] == "*":
                return dfs(i, j + 2) or first_match and dfs(i + 1, j)
            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)