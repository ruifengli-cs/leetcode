class Solution:
    # APP1: brute force, go row by row and col by col to find if it's in 2D matrix.
    # Time; O(n^2) space: O(1)

    # APP2: binary search row, then binary search col
    # Time: O(lg(m) + lg(n)) space: O(1) Runtime: 96%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # search row
        start_row, end_row, start_col, end_col = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while start_row + 1 < end_row:
            mid = (start_row + end_row) >> 1
            if matrix[mid][0] < target:
                start_row = mid
            else:
                end_row = mid
        final_row = start_row if matrix[end_row][0] > target else end_row
        # search col
        while start_col + 1 < end_col:
            mid = (start_col + end_col) >> 1
            if matrix[final_row][mid] <= target:
                start_col = mid
            else:
                end_col = mid
        return True if matrix[final_row][start_col] == target or matrix[final_row][end_col] == target else False

    # APP3: binary search from 0 to m * n - 1
    # Time: O(lg(mn)) == O(lg(m) + lg(n)) space: O(1) Runtime: 99%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) >> 1
            num = matrix[mid // n][mid % n]
            if num <= target:
                start = mid
            else:
                end = mid
        return True if matrix[start // n][start % n] == target or matrix[end // n][end % n] == target else False

    # APP4: optimize APP3 code using tighter bound. Runtime: 96%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        # 1. end should be m * n
        start, end = 0, m * n
        # 2. start < end
        while start < end:
            mid = (start + end) >> 1
            num = matrix[mid // n][mid % n]
            if num == target:
                return True
            elif num < target:
                # 3. start = mid + 1
                start = mid + 1
            else:
                end = mid
        return False

    # APP5: optimize APP2 code using bisect function. Runtime: 98%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # search row
        start_row, end_row = 0, len(matrix) - 1
        while start_row + 1 < end_row:
            mid = (start_row + end_row) >> 1
            if matrix[mid][0] < target:
                start_row = mid
            else:
                end_row = mid
        row_idx = start_row if matrix[end_row][0] > target else end_row
        # search col
        col_idx = bisect.bisect_left(matrix[row_idx], target)
        return True if col_idx < len(matrix[0]) and matrix[row_idx][col_idx] == target else False
