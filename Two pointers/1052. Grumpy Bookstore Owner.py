class Solution:
# APP1: one pass to find X continous unsatisfied, one pass to count max happy
# Time; O(n) space: O(1) Runtime: 84, memory: 100%
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers or not grumpy:
            return 0
        max_not_happy = 0
        total_happy = 0
        n = len(customers)
        left = right = 0
        while right < n and right < X:
            if grumpy[right] == 1:
                max_not_happy += customers[right]
            right += 1
        new_not_happy = max_not_happy
        while right < n:
            if grumpy[right] == 1:
                new_not_happy += customers[right]
            if grumpy[left] == 1:
                new_not_happy -= customers[left]
            max_not_happy = max(max_not_happy, new_not_happy)
            right += 1
            left += 1
        for i in range(n):
            if grumpy[i] == 0:
                total_happy += customers[i]
        return total_happy + max_not_happy
        
# APP2: sliding window one pass to find both for APP2
# Time; O(n) space: O(1) Runtime: 99%, memory: 100%
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers or not grumpy:
            return 0
        n = len(grumpy)
        total_happy = max_not_happy = now_not_happy = left = 0
        
        for right in range(n):
            if grumpy[right] == 0:
                total_happy += customers[right]
                continue
            now_not_happy += customers[right]
            while right - left >= X:
                if grumpy[left] == 1:
                    now_not_happy -= customers[left]
                left += 1
            max_not_happy = max(max_not_happy, now_not_happy)
        return max_not_happy + total_happy
