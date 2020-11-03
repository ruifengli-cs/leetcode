class Solution:
    # APP1: find all comb of cuts and get the min.
    # Time: O(n * 2^n) space: O(n) stack if doenst consider result

    # APP2: sequence DP: f[i]: min cuts for s[i:].
    # sice palin[i][j] depends on palin[i + 1][j - 1], we can calculate backwards.
    # f[i] = min(f[j]) + 1 for all i <= j < n if s[i:j] is palindrome.
    # we can pre-calculate is s[j: i + 1] is palindrome in O(n^2)
    # Time: O(n^2) space: O(n^2)
    # palin = [[1,1,0], [x,1,0],[x,x,1]]
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        # last one need to be -1 since later f[j + 1] + 1
        f, palin = [0] * n + [-1], [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i] = n - 1 - i
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or palin[i + 1][j - 1]):
                    palin[i][j] = True
                    # print(i, j)
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]
