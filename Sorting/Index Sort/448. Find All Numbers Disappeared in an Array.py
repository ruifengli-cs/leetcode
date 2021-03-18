class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        for i in range(n):
            val = abs(nums[i])
            nums[val - 1] = -abs(nums[val - 1])

        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res