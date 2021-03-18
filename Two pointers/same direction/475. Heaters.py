class Solution:
    # APP1: for each place, use binary search to find it's closest heater, compare the radius from left, right
    # Time: O(nlgm) space: O(1) n = len(places), m = len(heaters)

    # APP2: two pointers, cur, cur_heater. loop through places and find it's closest heater.
    # Time: O(n + m) if sorted, O(nlgn) if not sorted space: O(1) Runtime: 62%
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return 0
        houses.sort()
        heaters.sort()
        cur = cur_heater = 0
        m, n, res = len(houses), len(heaters), 0
        while cur < m and cur_heater < n:
            while cur_heater + 1 < n and heaters[cur_heater + 1] <= houses[cur]:
                cur_heater += 1
            radius = abs(heaters[cur_heater] - houses[cur])
            if cur_heater + 1 < n:
                radius = min(radius, abs(heaters[cur_heater + 1] - houses[cur]))
            res = max(res, radius)
            cur += 1

        if cur < m:
            res = max(res, abs(houses[-1] - heaters[cur]))

        return res