class Solution:
# APP1: brute force: Time: O(n^3) Space: O(1)
# Time: O(n^3) Space: O(1)
# Runtime: 6%, memory: 100%
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
#bug: m = len(B[0]) not len(B)
        n, m, k = len(A), len(B[0]), len(A[0])
        C = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for t in range(k):
                    C[i][j] += A[i][t] * B[t][j]
        return C 

# APP2: optimize the for loop order using A's sparsity
# Time: depend's on A's sparsity. worst: O(n^3) space: O(1)
# Runtime: 93% memory: 100%
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        n, m, k = len(A), len(B[0]), len(A[0])
        C = [[0] * m for _ in range(n)]
        for i in range(n):
            for t in range(k):
                if A[i][t] == 0:
                    continue
                for j in range(m):
                    C[i][j] += A[i][t] * B[t][j]
        return C 

# APP3: consider both A, B's sparsity, extract none 0 
# Time and space: depends on A,B's sparsity, worst: O(n^2)
# Runtime: 59% memory: 100%
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        sparse_A = self.get_none_zero(A)
        sparse_B = self.get_none_zero(B)
        n, m, k = len(A), len(A[0]), len(B[0])
        C = [[0] * k for _ in range(n)]
        for i, j, val_A in sparse_A:
            for x, y, val_B in sparse_B:
                if j == x:
                    C[i][y] += val_A * val_B
        return C
    
    def get_none_zero(self, A):
        res = []
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    continue
                res.append((i, j, A[i][j]))
        return res
        
        
# APP4: use row_vector and col_vector to extract none 0
# Time and space: depends on A,B's sparsity, worst: O(n^2)
# Runtime: 99%, Memory: 100
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        n, m, k = len(A), len(A[0]), len(B[0])
        row_vector = [
            [
                (j, A[i][j]) for j in range(m) if A[i][j] != 0
            ] 
            for i in range(n)
        ]
        
        col_vector = [
            [
                (i, B[i][j]) for i in range(m) if B[i][j] != 0
            ]
            for j in range(k)
        ]
        
        C = [
            [
                self.multi(row, col)
                for col in col_vector
            ] for row in row_vector
        ]

        return C
    
# Two pointers implementation 1    
    def multi(self, row, col):
        ans = 0
        i = 0
        for j in range(len(col)):
            while i < len(row) and row[i][0] < col[j][0]:
                i += 1
            if i < len(row) and row[i][0] == col[j][0]:
                ans += row[i][1] * col[j][1]
        return ans
# Two pointer implementation 2
    def multi(self, row, col):
        i = j = ans = 0
        n, m = len(row), len(col)
        while i < n and j < m:
            index_row, val_row = row[i]
            index_col, val_col = col[j]
            if index_row < index_col:
                i += 1
            elif index_row > index_col:
                j += 1
            else:
                ans += val_row * val_col
                i += 1
                j += 1
        return ans
