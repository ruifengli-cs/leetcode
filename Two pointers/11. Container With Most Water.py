class Solution:
    #     APP1: brute force. find all pairs and get the max water.
    #     Time: O(n^2) space: O(1)

    #     APP2: two pointers.
    #     Time: O(n) space: O(1)
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right, res = 0, len(height) - 1, 0
        while left < right:
            h = min(height[left], height[right])
            res = max(res, h * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res