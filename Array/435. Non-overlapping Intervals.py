class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        count = 0
        cur_start, cur_end = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            nxt_start, nxt_end = intervals[i][0], intervals[i][1]
            if cur_end > nxt_start:
                count += 1
            else:
                cur_start, cur_end = nxt_start, nxt_end
        return count

    # APP2: sort by starting position
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        count = 0
        cur_start, cur_end = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            nxt_start, nxt_end = intervals[i][0], intervals[i][1]
            if cur_end > nxt_start:
                count += 1
                if cur_end > nxt_end:
                    cur_start, cur_end = nxt_start, nxt_end
            else:
                cur_start, cur_end = nxt_start, nxt_end
        return count