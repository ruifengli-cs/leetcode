class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        word_set = set()
        for word in wordDict:
            word_set.add(word)
        memo = {}
        return self.dfs(s, word_set, memo)

    def dfs(self, s, word_set, memo):
        # return all sentences for s
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []
        ans = []
        for i in range(1, len(s)):
            if s[:i] not in word_set:
                continue
            for suffix in self.dfs(s[i:], word_set, memo):
                ans.append(s[:i] + " " + suffix)
        if s in word_set:
            ans.append(s)
        memo[s] = ans
        return ans

    # DFS no memoization. LTE
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         if not s:
#             return []
#         ans = []
#         path = []
#         self.dfs(s, wordDict, 0, path, ans)
#         return ans

#     def dfs(self, s, wordDict, start, path, ans):
# # return all paths for s[start:]
#         # if s[start:] in memo:
#         #     return memo[s[start:]]
#         if start == len(s):
#             ans.append(" ".join(path))
#         for word in wordDict:
#             n = len(word)
#             if start + n > len(s):
#                 continue
#             if word != s[start:start + n]:
#                 continue
#             path.append(word)
#             self.dfs(s, wordDict, start + n, path, ans)
#             path.pop()