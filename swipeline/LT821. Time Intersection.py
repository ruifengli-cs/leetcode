"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    def timeIntersection(self, seqA, seqB):
        if not seqA or not seqB:
            return []
        res = []
        online = start = end = 0
        points = []
        for seq in seqA:
            points.append((seq.start, 1))
            points.append((seq.end, -1))

        for seq in seqB:
            points.append((seq.start, 1))
            points.append((seq.end, -1))

        for point, val in sorted(points):
            if online == 2 and val == -1:
                end = point
                res.append(Interval(start, end))

            if online == 1 and val == 1:
                start = point
            online += val
        return res