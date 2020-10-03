class Solution:
    # APP1: count all elements, return most common one.
    # Time: O(nlgn) Space: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

    # APP2: hashmap two pass. first pass to get count. second pass to find count > n//2
    # Time: O(n) space: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        data = {}
        for num in nums:
            data[num] = data.get(num, 0) + 1
        for k, v in data.items():
            if v > len(nums) / 2:
                return k
        return 0