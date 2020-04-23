class Solution:
# APP1: Hashtable Time: O(n), Space: O(n). Runtime: 87% memory: 5%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        mapping = {}
        for index, val in enumerate(numbers):
            if target - val in mapping:
                return [mapping[target - val] + 1, index + 1]
            mapping[val] = index
        return [-1, -1]
        
# APP2: Two pointers. Time: O(n), Space: O(1). Runtime: 87% memory: 5%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        l, r = 0, len(numbers) - 1
        while l < r:
            now_sum = numbers[l] + numbers[r]
            if now_sum == target:
                return [l + 1, r + 1]
            elif now_sum < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]
        
# APP3: binary search. Time: O(nlgn) Space: O(1) Runtime: 15% memory: 5%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        for index, num in enumerate(numbers):
            pair_index = self.binary_search(target - num, index, numbers)
            if pair_index != -1:
                return [index + 1, pair_index + 1]
        return [-1, -1]
    
    def binary_search(self, num, start, numbers):
        end = len(numbers) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if numbers[mid] == num:
                return mid
            elif numbers[mid] < num:
                start = mid
            else:
                end = mid
        if numbers[start] == num:
            return start
        if numbers[end] == num:
            return end
        return -1
