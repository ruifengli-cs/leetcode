# [4,-3,-2,-7,8,2,-3,-1]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        res, n = set(), len(nums)
        for i in range(n):
            val = abs(nums[i])
            if nums[val - 1] < 0:
                res.add(val)
                continue

            nums[val - 1] = -abs(nums[val - 1])
        return list(res)