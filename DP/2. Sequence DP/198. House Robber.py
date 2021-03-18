class Solution:
    # APP1: DP f[i]: max money till house i
    # f[i][0] = max(f[i - 1][0], f[i - 1][1])
    # f[i][1] = nums[i] + f[i - 1][0]
    # Time: O(n) space: O(1) Runtime: 87%
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pick, not_pick, n = nums[0], 0, len(nums)
        for i in range(1, n):
            pick, not_pick = nums[i] + not_pick, max(pick, not_pick)
        return max(pick, not_pick)