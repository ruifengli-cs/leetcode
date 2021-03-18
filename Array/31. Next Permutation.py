# APP1: brute force. loop backwards, for each element i, loop again backwards find first j > i. swap them.
# if not, sort the array.
# Time: O(n^2) space: O(1)

# APP2:
# 1. backwardsly, find first decreasing point cur,
# 2. then find first bigger item that j > cur, swap them.
# 3. then reverse all element after cur.
# Time: O(n) space: O(1) runtime: 92%
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        cur = n - 2
        # 1. backwardsly, find first decreasing point cur,
        while cur >= 0 and nums[cur] >= nums[cur + 1]:
            cur -= 1
        # print(cur)

        # 2. then find first bigger item that j > cur, swap them.
        j = cur
        while j + 1 < n and nums[j + 1] > nums[cur]:
            j += 1
        if cur != -1:
            nums[cur], nums[j] = nums[j], nums[cur]

        # 3. then reverse all element after cur.
        left, right = cur + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1