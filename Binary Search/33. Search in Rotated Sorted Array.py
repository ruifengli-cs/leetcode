class Solution:
    def search(self, A: List[int], target: int) -> int:
        if not A or target is None:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) >> 1
            if A[mid] >= A[0]:
                if A[mid] <= target:
                    start = mid
                else:
                    if target >= A[0]:
                        end = mid
                    else:
                        start = mid
            else:
                if A[mid] >= target:
                    end = mid
                else:
                    if target >= A[0]:
                        end = mid
                    else:
                        start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1