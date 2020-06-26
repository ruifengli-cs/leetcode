class Solution:
    # APP1: brute force: use set to avoid duplicates, sort the ans before put it in the set, no need to sort the array
    # Time: O(n^3) space: O(1) Runtime: TLE
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        n, res = len(nums), set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return list(res)

    # APP2: hashmap a + b + c = 0 means a + b = -c, just like two sum
    # for each num: c, see if we can find a + b = -c
    # Time: O(n^2) Space: O(n) Runtime: 2s, 5% Memory: 17mb 34%
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n - 2):
            mapping, target = {}, -nums[i]
            for j in range(i + 1, n):
                if target - nums[j] in mapping:
                    res.add((-target, nums[mapping[target - nums[j]]], nums[j]))
                else:
                    mapping[nums[j]] = j
        return list(res)

    # APP3: sort the list, for each target, use two pointers in opposite direction like two sum
    # TIme: O(n^2) Space: O(1) Runtime: 31%
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        res, n = set(), len(nums)
        for i in range(n - 2):
            target, l, r = -nums[i], i + 1, n - 1
            while l < r:
                now_sum = nums[l] + nums[r]
                if now_sum == target:
                    res.add((-target, nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif now_sum < target:
                    l += 1
                else:
                    r -= 1
        return list(res)
