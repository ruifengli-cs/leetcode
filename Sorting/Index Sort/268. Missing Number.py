# 9:40
# APP1: use index to store existing as negative
# if nums[val] == n, continue
# if nums[val] == 0, set index 0 neg, then set nums[val] = -n so that it doesnt impact other idx
# Time: O(n) space: O(1) runtime: 29%
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        for val in nums:
            val = abs(val)
            if val == n:
                continue
            if nums[val] != 0:
                nums[val] = -abs(nums[val])
            else:
                nums[0] = -abs(nums[0])
                nums[val] = -n
        for i in range(n):
            if nums[i] >= 0:
                return i
        return n
# 9:46