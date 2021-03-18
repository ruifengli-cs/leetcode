# APP1: iterate through num for start, then use right pointer to get now_sum and find first right.
# Time: O(n^2) space: O(1)

# APP2: two pointers. once nowsum reach s, decrease nums[left]
# Time: O(n) space: O(1) Runtime: 96

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or s is None:
            return 0
        res, n, nowsum, left = sys.maxsize, len(nums), 0, 0
        for i in range(n):
            nowsum += nums[i]
            while nowsum >= s and left <= i:
                res = min(res, i - left + 1)
                nowsum -= nums[left]
                left += 1
        return res if res != sys.maxsize else 0    