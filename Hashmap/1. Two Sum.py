class Solution:
# APP1: brute force, nested loop find all combination 
# Time: O(n^2), space: O(1) Runtime: TLE
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
                
                
# APP2: sort the list, use two pointers, can also use binary search
# Time: O(nlgn) Space: O(n) Runtime: 54% Space: 5%
# bug: need to store original index
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        sorted_nums = []
# bug1: forget enumerate
        for index, num in enumerate(nums):
            sorted_nums.append((num, index))
# bug2: didn't spell lambda correctly, also no space for key=lambda
        sorted_nums = sorted(sorted_nums, key=lambda x: x[0])
        l, r = 0, len(nums) - 1
        while l < r:
            now_sum = sorted_nums[l][0] + sorted_nums[r][0]
            if now_sum < target:
                l += 1
            elif now_sum > target:
                r -= 1
            else:
                return [sorted_nums[l][1], sorted_nums[r][1]]
        return [-1, -1]
        
# APP3: use Hashmap two pass
# Time: O(n) Space: O(N) Runtime: 77% memory: 5
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        mapping = {}
        for index, num in enumerate(nums):
            mapping[num] = index
        for index, num in enumerate(nums):
            if target - num in mapping and mapping[target - num] != index:
                return [index, mapping[target - num]]
        return [-1, -1]
    
# APP4: use hashmap one pass
# Time: O(n) Space: O(N) Runtime: 77% memory: 5
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        mapping = {}
        for index, num in enumerate(nums):
            if target - num in mapping:
                return [mapping[target - num], index]
            mapping[num] = index
        return [-1, -1]
