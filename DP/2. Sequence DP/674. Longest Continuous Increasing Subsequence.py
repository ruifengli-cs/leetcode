# APP1: iterate nums for starting pos, find LCIS for it. compare lengths.
# Time: O(n^2) space: O(1)

# APP2: two pointers. find LCIS till the dropping point, then start again.
# Time: O(n) space: O(1) runtime: 90%
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start = end = res = 0
        n = len(nums)
        while end < n:
            while end + 1 < n and nums[end + 1] > nums[end]:
                end += 1
            res = max(res, end - start + 1)
            end += 1
            start = end
        return res

# APP3: DP def: f[i]: LCIS ending with i.
# f[i] = max(1, f[i - 1]|nums[i - 1] < nums[i])
# Time: O(n) space: O(n) -> O(1) runtime: 90%
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        cur = pre_len = res = 1
        for i in range(1, n):
            cur = 1
            if i > 0 and nums[i] > nums[i - 1]:
                cur = max(cur, pre_len + 1)
            res = max(res, cur)
            pre_len = cur
        return res








