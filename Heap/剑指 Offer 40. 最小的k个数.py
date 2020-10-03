import heapq


class Solution:
    # APP1: put them in set, sort it, output smallest k.
    # Time: O(nlgn) space: O(n)
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or not k or k < 0:
            return []
        return sorted(arr)[:k]

    # APP2: use heap.
    # Time: O(n) space: O(k)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or not k or k < 0:
            return []
        max_heap, res = [], []
        for num in arr:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -num)
                continue
            if num < -max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -num)
        while max_heap:
            res.append(-heapq.heappop(max_heap))
        return res[::-1]