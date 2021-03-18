# APP1:
# just like house robber, we can get 0 to n - 2 and 1 to n - 1. then find max.
# Time: O(n) space: O(1) Runtime: 94%
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.houserobber(nums, 0, n - 2), self.houserobber(nums, 1, n - 1))

    def houserobber(self, nums, start, end):
        pick, not_pick = nums[start], 0
        for i in range(start + 1, end + 1):
            pick, not_pick = nums[i] + not_pick, max(pick, not_pick)
        return max(pick, not_pick)