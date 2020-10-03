import heapq


class Solution:
    # APP1: minheap. since each row is sorted. put first element of each row in the minheap. then pop k times.
    # Time: O(xlgn) + O(x) Space: O(X) . X = min(k, n),
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if not matrix or not matrix[0] or k is None or k < 0 or k > n * n:
            return -1
        minheap = []
        size = min(k, n)
        for i in range(size):
            minheap.append((matrix[i][0], i, 0))
        heapq.heapify(minheap)
        for _ in range(k):
            val, x, y = heapq.heappop(minheap)
            if y < n - 1:
                heapq.heappush(minheap, (matrix[x][y + 1], x, y + 1))
        return val

    # APP2: binary search answer. TIme: O(nlg(max - min)) space: O(1)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if not matrix or not matrix[0] or not k or k < 0 or k > n * n:
            return -1
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            count = self.find_count_less(matrix, mid)
            if count < k:
                start = mid
            else:
                end = mid
        if self.find_count_less(matrix, end) < k:
            return end
        if self.find_count_less(matrix, start) < k:
            return start
        return -1

    def find_count_less(self, matrix, num):
        n = len(matrix)
        i, j, count = 0, n - 1, 0
        while i < n and j >= 0:
            if matrix[i][j] >= num:
                j -= 1
            else:
                count += j + 1
                i += 1
        return count






