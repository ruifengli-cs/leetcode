class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        first = bisect.bisect_left(nums, target)
        second = bisect.bisect_right(nums, target) - 1
        if first > n - 1 or second > n - 1 or nums[first] != target or nums[second] != target:
            return [-1, -1]
        return [first, second]