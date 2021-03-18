# dp[i]: min deletions from 0 to i
# use bcount to count how manu b we need remove previously
# if s[i] == "a": we either keep "a"(delete all "b"), or delete "a".
# dp[i] = min(bcount, 1 + dp[i - 1])
# else: we can always append "b".
# dp[i] = dp[i - 1], bcount + 1
# Time: O(n) space: O(n) runtime: 52%
class Solution:
    def minimumDeletions(self, s: str) -> int:
        if not s or len(s) == 1:
            return 0
        n, b_cnt = len(s), 0
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if s[i - 1] == "a":
                dp[i] = min(b_cnt, 1 + dp[i - 1])
            else:
                dp[i] = dp[i - 1]
                b_cnt += 1
        return dp[n]