# APP1: recursion + two pointers
# Time: O(2^n) space: O(2^n)
# 1 + 2 + 4 + ... + 2^n
class Solution:
    def countAndSay(self, n: int) -> str:
        if not n or n < 0:
            return ""
        res = self.dfs(['1'], n)
        return ''.join(res)

    def dfs(self, seq, n):
        if n == 1:
            return seq
        res = []
        left, count = 0, 1
        for i in range(1, len(seq)):
            if seq[i] == seq[left]:
                count += 1
                continue
            res.append(str(count))
            res.append(str(seq[i - 1]))
            left, count = i, 1
        res.append(str(count))
        res.append(str(seq[-1]))
        return self.dfs(res, n - 1)