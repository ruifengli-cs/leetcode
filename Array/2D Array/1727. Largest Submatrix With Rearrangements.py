# APP1: loop through each row and col, for each cell, add above 1's.
# sort it by row after each row, then look left to compute max submatrix.
# Time: O(mn) space: O(m) Runtime: 85%
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and matrix[i][j] == 1:
                    matrix[i][j] = matrix[i - 1][j] + 1
            cur_row = sorted(matrix[i], reverse=True)
            for k in range(n):
                ans = max(ans, cur_row[k] * (k + 1))
        return ans