# APP1: create 2D matrix. every snap, copy entire array
# TIme: O(n * snap) space: O(n * snap) runtime: TLE
# class SnapshotArray:

#     def __init__(self, length: int):
#         self.matrix = [[0] * length]

#     def set(self, index: int, val: int) -> None:
#         self.matrix[-1][index] = val

#     def snap(self) -> int:
#         self.matrix.append(copy.deepcopy(self.matrix[-1]))
#         return len(self.matrix) - 2

#     def get(self, index: int, snap_id: int) -> int:
#         return self.matrix[snap_id][index]

# APP2: instead of copy entire array. only append changed to that element
# Time: O(n) space: O(n) Runtime: 47%
class SnapshotArray:

    def __init__(self, length: int):
        self.matrix = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.matrix[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect(self.matrix[index], [snap_id + 1]) - 1
        return self.matrix[index][idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)