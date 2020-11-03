class Solution:
    # APP1: dfs. each time you can include cur ch to previous or start a new string.
    # TIme:O(n*2^n) space: O(2^n) Runtime: 23.8%
    #     def partition(self, s: str) -> List[List[str]]:
    #         if not s:
    #             return [[]]
    #         res = []
    #         self.dfs(s, res, [], s[0], 1)
    #         return res

    #     def dfs(self, s, res, path, cur_palin, cur):
    #         if cur == len(s):
    #             if not self.is_palin(cur_palin):
    #                 return
    #             path.append(cur_palin)
    #             res.append(path[:])
    #             path.pop()
    #             return
    #         self.dfs(s, res, path, cur_palin + s[cur], cur + 1)
    #         if self.is_palin(cur_palin):
    #             path.append(cur_palin)
    #             self.dfs(s, res, path, s[cur], cur + 1)
    #             path.pop()

    #     def is_palin(self, s):
    #         start, end = 0, len(s) - 1
    #         while start < end:
    #             if s[start] != s[end]:
    #                 return False
    #             start += 1
    #             end -= 1
    #         return True

    # APP2: dfs + DP.
    # f[i]: from start to i all possible palindrome partitions.
    # f[i] = f[i - 1] + s[] Runtime: 99.26%
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        n = len(s)
        res, dp = [], [[0] * n for _ in range(n)]
        self.dfs(s, res, [], dp, 0)
        return res

    def dfs(self, s, res, path, dp, idx):
        if idx >= len(s):
            res.append(path[:])
        for end in range(idx, len(s)):
            if s[idx] == s[end] and (end - idx < 2 or dp[idx + 1][end - 1]):
                dp[idx][end] = True
                path.append(s[idx:end + 1])
                self.dfs(s, res, path, dp, end + 1)
                path.pop()
