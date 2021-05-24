class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        mapping = {}
        return self.dfs(p, s, 0, 0, mapping)

    def dfs(self, p, s, i, j, mapping):
        if i == len(p) and j == len(s):
            return True
        if i == len(p) or j == len(s):
            return False
        if p[i] in mapping:
            if mapping[p[i]] != s[j:j + len(mapping[p[i]])]:
                return False
            else:
                return self.dfs(p, s, i + 1, j + len(mapping[p[i]]), mapping)

        # p[i] not in mapping
        for k in range(j + 1, len(s) + 1):
            if s[j:k] in mapping.values():
                continue
            mapping[p[i]] = s[j:k]
            if self.dfs(p, s, i + 1, k, mapping):
                return True
            del mapping[p[i]]
        return False