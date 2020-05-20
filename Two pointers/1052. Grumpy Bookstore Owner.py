class Solution:
    # APP1: brute force: loop through starting position for x.
    # time: O(nX) Space: O(1) Runtime: TLE
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers or not grumpy:
            return 0
        #       find total satified customers when grumpy is 0
        total_not_grumpy, n = 0, len(customers)
        for i in range(n):
            if not grumpy[i]:
                total_not_grumpy += customers[i]
        #       find max satisfied customers when grumpy
        max_grumpy = 0
        for i in range(n):
            now_grumpy = 0
            for j in range(X):
                new_idx = i + j
                if new_idx < n and grumpy[new_idx]:
                    now_grumpy += customers[new_idx]
            max_grumpy = max(max_grumpy, now_grumpy)
        return total_not_grumpy + max_grumpy

    # APP2: sliding window to find happy customers when grumpy
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers or not grumpy:
            return 0

        total_not_grumpy, n = 0, len(customers)
        max_grumpy = l = now_grumpy = 0
        for r in range(n):
            #       find total satified customers when not grumpy
            if not grumpy[r]:
                total_not_grumpy += customers[r]
                continue

            #       find total satified customers when grumpy
            now_grumpy += customers[r]
            while r - l + 1 > X:
                if grumpy[l]:
                    now_grumpy -= customers[l]
                l += 1
            max_grumpy = max(max_grumpy, now_grumpy)
        return total_not_grumpy + max_grumpy
