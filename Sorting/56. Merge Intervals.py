class Solution:
    #     APP1: brute force. compare each one with the res
    #     Time: O(n^2) space: O(n) to store the res

    #     APP2: sort the intervals by starting pos, compare end with next start
    #     Time: O(nlgn) space: O(n) to store the res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for s, e in sorted(intervals):
            if res and s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        return res

    # previous version.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return []
        res, n = [], len(intervals)
        intervals.sort()
        start, end = intervals[0]
        for s, e in intervals:
            if s <= end:
                end = max(end, e)
            else:
                res.append([start, end])
                start, end = s, e
        res.append([start, end])
        return res