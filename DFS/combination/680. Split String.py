# Solution1: dfs + memoization
import copy
from functools import lru_cache


class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        res = []
        if not s:
            res.append([])
            return res
        n = len(s)
        path = []

        def dfs(idx):
            if idx == n:
                res.append(copy.deepcopy(path))
                return

            path.append(s[idx])
            dfs(idx + 1)
            path.pop()

            if idx < n - 1:
                path.append(s[idx: idx + 2])
                # print(path, idx)
                dfs(idx + 2)
                path.pop()

        dfs(0)
        return res