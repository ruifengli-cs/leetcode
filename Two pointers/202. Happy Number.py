# Attemp1: recurssion. TLE if it's not True
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         if not n or n == 1:
#             return True
#         res = digit = 0
#         while n:
#             digit = n % 10
#             res += digit * digit
#             n = n // 10
#         return True if res == 1 else self.isHappy(res)

# APP1: use set to see if it's been seen
# Time: O(n) space: O(n) Runtime: 84%
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         if not n or n == 1:
#             return True
#         seen = set()
#         while n != 1 and n not in seen:
#             seen.add(n)
#             n = self.next_happy(n)
#         return True if n == 1 else False

#     def next_happy(self, n):
#         res = digit = 0
#         while n:
#             digit = n % 10
#             res += digit * digit
#             n = n // 10
#         return res

# APP2: two pointers to reduce space to O(1)
# Time: O(n) space: O(1) Runtime: 61%
class Solution:
    def isHappy(self, n: int) -> bool:
        if not n or n == 1:
            return True
        slow, fast = n, n
        while fast != 1:
            slow = self.next_happy(slow)
            fast = self.next_happy(self.next_happy(fast))
            if slow != 1 and slow == fast:
                return False
        return True

    def next_happy(self, n):
        res = digit = 0
        while n:
            digit = n % 10
            res += digit * digit
            n = n // 10
        return res