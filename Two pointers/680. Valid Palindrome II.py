class Solution:
# APP0: brute force: for each of the char, form a new string without cur char and check palindrom
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        for i in range(n):
            new_s = s[:i] + s[i + 1:]
            if self.is_palin(new_s):
                return True
        return False

    def is_palin(self, s):
        if not s or len(s) < 2:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            return True
#APP1: Recursion. TIme: O(n) Space: O(1)
# Runtime: 8%, memory: 6%
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.is_palin(s, left + 1, right) or self.is_palin(s, left, right - 1)
            left += 1
            right -= 1
        return True
    
    def is_palin(self, s, start, end):
        if start < 0 or start > len(s) - 1 or end < 0 or end > len(s) - 1:
            return True
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return self.is_palin(s, start + 1, end - 1)
        
#APP2: Two pointer opposite direction. Time: O(n) Space: O(1)
# Runtime: 49%, memory: 6%
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.is_palin(s, left + 1, right) or self.is_palin(s, left, right - 1)
            left += 1
            right -= 1
        return True
    
    def is_palin(self, s, start, end):
        l, r = start, end
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
#APP3: Compare substring Time: O(n) Space: O(n) worst
# Runtime: 73%, memory: 6%
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                s1, s2 = s[l + 1: r + 1], s[l: r]
                return s1 == s1[::-1] or s2 == s2[::-1]
            l += 1
            r -= 1
        return True
