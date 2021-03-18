# APP2: optimized dfs + memoization. since we can get r from l and idx. we only need two dimensions
# Time: O(mn) space: O(mn)
class Solution:
    def maximumScore(self, nums: List[int], A: List[int]) -> int:
        if not nums or not A:
            return 0
        n, m = len(nums), len(A)

        @lru_cache(2000)
        def dfs(l, idx):
            if idx == m:
                return 0
            pick_left = dfs(l + 1, idx + 1) + nums[l] * A[idx]
            pick_right = dfs(l, idx + 1) + nums[n - 1 - (idx - l)] * A[idx]
            return max(pick_left, pick_right)

        return dfs(0, 0)

