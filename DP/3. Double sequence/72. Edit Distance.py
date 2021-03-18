# APP1: dfs(i, j) min operations to convert word1[:i] to word2[:j]
# if w1[i] == w2[j]: return dfs(i + 1, j + 1)
# else return min(dfs(i - 1, j), dfs(i - 1, j - 1), dfs(i, j - 1)) + 1

# APP2: DP.
# def: f[i][j]: min operations convert w1[:i] to w2[:j]
# fuction: f[i][j] = f[i - 1][j - 1] if w1[i] == w2[j]
#          f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1 if w1[i] != w2[j]
# init: f[0][j] = j, f[i][0] = i
# ans: f[m][n]
# Time: O(n^2) space: O(n^2) -> O(n) runtime: 72%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) or len(word2)
        m, n = len(word1), len(word2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        # init
        for i in range(m + 1):
            f[i][0] = i
        for j in range(n + 1):
            f[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
        return f[m][n]


# APP3: Optimize it using one dimension array. Runtime: 84%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) or len(word2)
        m, n = len(word1), len(word2)
        # init
        old = [i for i in range(n + 1)]
        new = old[:]

        for i in range(1, m + 1):
            new[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    new[j] = old[j - 1]
                else:
                    new[j] = min(old[j - 1], old[j], new[j - 1]) + 1
            old, new = new, old
        return old[n]


# APP4: we can also use max(w1, w2) - lcs(w1, w2)