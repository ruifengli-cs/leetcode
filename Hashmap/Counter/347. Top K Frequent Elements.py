class Solution:
    # APP1: use Counter and get most_common k elements
    # Time: O(n + NlgN) N = unique numbers. space: O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k or k < 0:
            return []
        res, count = [], collections.Counter(nums)
        for num, freq in count.most_common(k):
            res.append(num)
        return res

    # APP2: one liner
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in collections.Counter(nums).most_common(k)]