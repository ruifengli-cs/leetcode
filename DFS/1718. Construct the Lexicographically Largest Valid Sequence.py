# APP1: dfs. fill the position from biggest
# Time: NP problem. O(n^n) space: O(n)
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if not n or n < 0:
            return []
        res, used = [0] * (2 * n - 1), [0] * (n + 1)
        self.dfs(n, 0, res, used)
        return res

    def dfs(self, n, idx, res, used):
        if idx == 2 * n - 1:
            return True
        if res[idx] > 0:
            return self.dfs(n, idx + 1, res, used)
        for i in range(n, 0, -1):
            # if idx + i out bound, res[idx + i] already has number, cur is used, i != 1
            if used[i] > 0:
                continue
            if i > 1 and (idx + i >= 2 * n - 1 or res[idx + i] > 0):
                continue

            res[idx] = i
            if i > 1 and idx + i < 2 * n - 1:
                res[idx + i] = i
            used[i] = 1
            if self.dfs(n, idx + 1, res, used):
                return True
            res[idx] = 0
            if i > 1 and idx + i < 2 * n - 1:
                res[idx + i] = 0
            used[i] = 0
        return False