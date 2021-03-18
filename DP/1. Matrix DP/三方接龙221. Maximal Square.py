# APP1: for each (i, j), check it's (i -1, j), (i - 1, j - 1), (i, j - 1) to see if it's a square.
# Time: O(mn * mnk) space: O(mn)

# APP2: dp. f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1, ans: max(f[i][j])
# Time: O(mn) space: O(mn)-> O(n)
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix or not matrix[0]:
#             return 0
#         m, n, res = len(matrix), len(matrix[0]), 0
#         f = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if matrix[i - 1][j - 1] == '0':
#                     continue
#                 f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
#                 res = max(res, f[i][j])
#         return res * res

# APP3: optimize space useing one dimension array
# Time: O(mn) space: O(n) runtime: 80%
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n, res = len(matrix), len(matrix[0]), 0
        new, old = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '0':
                    # bug: remember to set to 0 for new[j]
                    new[j] = 0
                    continue
                new[j] = min(old[j], new[j - 1], old[j - 1]) + 1
                res = max(res, new[j])
            new, old = old, new
        return res * res


