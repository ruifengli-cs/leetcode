# APP1: DFS + memoization
# Time: O(2^min(n,m)) space: O(min(m, n))
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return s is "" or s is None
        return self.dfs(s, 0, p, 0)

    @lru_cache(2000)
    def dfs(self, s, i, p, j):
        if j == len(p):
            return i == len(s)
        if i > len(s):
            # print(p[j] in ["?", "*"])
            return False
        if p[j] == "?":
            return self.dfs(s, i + 1, p, j + 1)
        if p[j] != "*":
            if i >= len(s):
                return False
            return s[i] == p[j] and self.dfs(s, i + 1, p, j + 1)
        return self.dfs(s, i, p, j + 1) or self.dfs(s, i + 1, p, j + 1) or self.dfs(s, i + 1, p, j)