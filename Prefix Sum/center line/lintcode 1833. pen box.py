class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """

    # APP1: Brute force: for each index, find the first valid subarray, then find second
    # Use two pointers in same direction to find one valid subarray
    # Time: O(n^2) space: O(1) Runtime: TLE
    def minimumBoxes(self, boxes, target):
        if not boxes or target is None or target < 0:
            return -1
        n = len(boxes)
        min_len = n + 1

        for i in range(n):
            first_start, first_end = self.find_valid(boxes, target, i)
            second_start, second_end = self.find_valid(boxes, target, first_end + 1)
            if first_start != -1 and second_start != -1:
                min_len = min(min_len, first_end - first_start + 1 + second_end - second_start + 1)
        if min_len == n + 1:
            return -1
        return min_len

    def find_valid(self, boxes, target, start):
        now_sum = 0
        end, n = start, len(boxes)
        while end < n:
            now_sum += boxes[end]
            while now_sum > target:
                now_sum -= boxes[start]
                start += 1
            if now_sum == target:
                return (start, end)
            end += 1
        return (-1, -1)

    # APP2: for each index, find it's left_min and right_min
    def minimumBoxes(self, boxes, target):
        if not boxes or target is None or target < 0:
            return -1
        n = len(boxes)
        min_len = n + 1

        for i in range(n - 1):
            left_min = self.find_valid(boxes, target, 0, i)
            right_min = self.find_valid(boxes, target, i + 1, n - 1)
            if left_min != -1 and right_min != -1:
                min_len = min(min_len, left_min + right_min)
        if min_len == n + 1:
            return -1
        return min_len

    def find_valid(self, boxes, target, start, end):
        now_sum = 0
        left = start
        for right in range(start, end + 1):
            now_sum += boxes[right]
            while now_sum > target:
                now_sum -= boxes[left]
                left += 1
            if now_sum == target:
                return right - left + 1
        return -1

    # APP3: pre-process left_min and right_min for each index
    def minimumBoxes(self, boxes, target):
        if not boxes or target is None or target < 0:
            return -1
        n = len(boxes)
        min_len = n + 1
        left_min = self.find_valid(boxes, target)
        right_min = self.find_valid(boxes[::-1], target)
        right_min.reverse()
        for i in range(n):
            if left_min[i] != n + 1 and right_min[i] != n + 1:
                min_len = min(min_len, left_min[i] + right_min[i + 1])
        if min_len == n + 1:
            return -1
        return min_len

    def find_valid(self, boxes, target):
        res = []
        n = len(boxes)
        left = now_sum = 0
        min_len = n + 1
        for right in range(n):
            now_sum += boxes[right]
            while now_sum > target:
                now_sum -= boxes[left]
                left += 1
            if now_sum == target:
                min_len = min(min_len, right - left + 1)
            res.append(min_len)
        return res