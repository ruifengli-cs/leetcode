from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        n = len(s)

        @lru_cache(2000)
        def dfs(idx):
            if idx == n:
                return True
            for i in range(idx + 1, n + 1):
                if s[idx: i] not in wordDict:
                    continue
                if dfs(i):
                    return True

        return dfs(0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        memo = {}
        return self.dfs(s, wordDict, 0, memo)

    def dfs(self, s, wordDict, start, memo):
        # return if s[start:] can be made of wordDict
        if s[start:] in memo:
            return memo[s[start:]]
        if start == len(s):
            return True

        for word in wordDict:
            n = len(word)
            if start + n > len(s):
                continue
            # I should not return if if dfs didn't find it. I should skip the current word and continue to use next word
            if word != s[start:start + n]:
                continue
            # same here, I need use it as a condition instead of directly return
            if self.dfs(s, wordDict, start + n, memo):
                memo[s[start + n:]] = True
                return True
            memo[s[start + n:]] = False
        return False
