"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    # APP1: loop through input, get count of overlapping ones.
    # Time: O(n^2) space: O(1)

    # APP2: swipeline. add input into points: [start, 1], [end, -1]
    # sort points and count
    # Time: O(nlgn) space: O(n)
    def countOfAirplanes(self, airplanes):
        if not airplanes:
            return 0

        # restructure input
        points = []
        for plane in airplanes:
            points.append((plane.start, 1))
            points.append((plane.end, -1))

        # swipeline to get max count
        cur_planes = max_planes = 0
        for _, status in sorted(points):
            cur_planes += status
            max_planes = max(max_planes, cur_planes)

        return max_planes