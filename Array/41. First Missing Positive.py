# APP1: using hashmap.
# Time: O(n) space: O(n)
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         if not nums:
#             return 1
#         unique = set()
#         for val in nums:
#             if val <= 0:
#                 continue
#             unique.add(val)

#         for i in range(1, len(nums) + 2):
#             if i not in unique:
#                 return i
#         return 1

# APP2: use constant space. max missing res is n + 1 where n = len(nums) like 1,2,3,4. missing 5
# 1. first pass: check if 1 is not present, if not, then return 1
# 2. second pass: change all negative and 0 to 1 use negative to mark the existing element in nums.
# 3. third pass: find first positive number after index 0
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1

        # [1]
        if n == 1:
            return 2

        # make all neg and 0 to 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # mark neg for existing, use idx 0 for nth
        for i in range(n):
            val = abs(nums[i])
            if val != n:
                nums[val] = -abs(nums[val])
            else:
                nums[0] = -abs(nums[0])

        # find first positive
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n

        return n + 1