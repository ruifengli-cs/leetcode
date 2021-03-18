# APP1: if nothing is missing. array should be [1,2,3,4,5], then missing n + 1
# if nums[i] > n, then must be a missing number between 1-n.
# 1: first check 1 in nums
# 2: make 0 and neg and nums[i] > n as 1
# 3: use index as negative to mark existing value. use index 0 to store n
# 4: find first positive index.
# 9:09
# assume I can modify the origianl array
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or 1 not in nums:
            return 1
        n = len(nums)
        # 2. mark 0 and neg
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # step 3
        for i in range(n):
            if abs(nums[i]) == n:
                nums[0] = -abs(nums[0])
            else:
                val = abs(nums[i])
                nums[val] = -abs(nums[val])
        # step4
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1
# 9:17