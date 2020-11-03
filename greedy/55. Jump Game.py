class Solution:
    # APP1: greedy. loop through array to find max index to reach
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        max_idx, n = 0, len(nums)
        for i, val in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + val)
            if max_idx >= n - 1:
                return True
        return False