class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an long integer,denote the number of topologicalsort
    """
    def topologicalSortNumber(self, n, p):
        # Write your code here
        son = [0] * n
        for i in range(len(p)):
            x, y = p[i][1], p[i][0]
            son[x] |= 1 << y
        lim = 1 << n
        dp = [0] * lim
        dp[0] = 1
        for i in range(lim):
            for j in range(n):
                if (i & son[j]) == son[j] and (i & (1 << j)) == 0:
                    dp[i | (1 << j)] += dp[i]
        return dp[lim - 1]