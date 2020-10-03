class Solution:
    # APP1: dfs, TIme: O(2^n) Space: O(n) Runtime: TLE
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            if not text1 or not text2:
                return 0
            return self.dfs(text1, 0, text2, 0)

        def dfs(self, s1, p1, s2, p2):
            if p1 > len(s1) - 1 or p2 > len(s2) - 1:
                return 0
            if s1[p1] == s2[p2]:
                return 1 + self.dfs(s1, p1 + 1, s2, p2 + 1)
            return max(self.dfs(s1, p1 + 1, s2, p2), self.dfs(s1, p1, s2, p2 + 1))

    # APP2: DFS + memoization
    # Time: O(n*m) Space: O(n*m) Runtime: 9%
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            if not text1 or not text2:
                return 0
            memo = {}
            return self.dfs(text1, 0, text2, 0, memo)

        def dfs(self, s1, p1, s2, p2, memo):
            if p1 >= len(s1) or p2 >= len(s2):
                return 0
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            if s1[p1] == s2[p2]:
                memo[(p1, p2)] = 1 + self.dfs(s1, p1 + 1, s2, p2 + 1, memo)
            else:
                memo[(p1, p2)] = max(self.dfs(s1, p1 + 1, s2, p2, memo), self.dfs(s1, p1, s2, p2 + 1, memo))

            return memo[(p1, p2)]

    # APP3: DP f[i][j]: LCS from 0,0 to i, j.
    # f[i][j] = if s1[i] == s2[j]: 1 + f[i - 1][j - 1] else max(f[i][j - 1], f[i - 1][j])
    # Time: O(n*m) Space: O(n*m) Runtim: 60%
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            if not text1 or not text2:
                return 0
            m, n = len(text1) + 1, len(text2) + 1
            f = [[0] * n for _ in range(m)]
            for i in range(1, m):
                for j in range(1, n):
                    if text1[i - 1] != text2[j - 1]:
                        f[i][j] = max(f[i][j - 1], f[i - 1][j])
                    else:
                        f[i][j] = f[i - 1][j - 1] + 1

            return f[m - 1][n - 1]

    # APP4: optimize APP3 using rolling array
    # Time: O(m*n) Space: O(min(m, n)) Runtime: 95%
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m, n = len(text1) + 1, len(text2) + 1
        old, new = [0] * n, [0] * n
        for i in range(1, m):
            for j in range(1, n):
                if text1[i - 1] != text2[j - 1]:
                    new[j] = max(new[j - 1], old[j])
                else:
                    new[j] = old[j - 1] + 1
            old, new = new, old
        return old[n - 1]

    # APP5: DP dp[i][j] lcs for str1[i1:] and str2[i2:]
    # dp[i][j] = dp[i + 1][j + 1] + 1 if str1[i] == str2[j] else max(dp[i][j + 1], dp[i + 1][j])
    # cur, old = [0] * n, [0] * n


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m, n = len(text1), len(text2)
        cur, old = [0] * (n + 1), [0] * (n + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = old[j + 1] + 1
                else:
                    cur[j] = max(cur[j + 1], old[j])
            cur, old = old, cur
        return old[0]
