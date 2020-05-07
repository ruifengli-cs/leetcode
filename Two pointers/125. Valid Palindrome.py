class Solution:
# AAP1: reverse string, compare new with old
# Time: O(n) Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        lower_s = ""
        for ch in s:
            if ch.isalnum():
                lower_s += ch.lower()
        reversed_s = lower_s[::-1]
        for i in range(len(lower_s)):
            if lower_s[i] != reversed_s[i]:
                return False
        return True
        
        
# APP2: recurssion. Downside is it will stack overflow when string is too long
# Time; O(n) Space: O(n)
# Runtime: MLE
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        lower_s = ""
        for ch in s:
            if not ch.isalnum():
                continue
            lower_s += ch.lower()
        return self.is_palin(lower_s)
    
    def is_palin(self, s):
        if not s:
            return True
        if s[0] != s[-1]:
            return False
        return self.is_palin(s[1: -1])
        
# APP3: two pointers
# Time; O(n) Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
# Reverse original string and loop through it
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        s1 = s[::-1]
        cur_s1 = 0
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            while not s1[cur_s1].isalnum():
                cur_s1 += 1
            if s[i].lower() != s1[cur_s1].lower():
                return False
            cur_s1 += 1
        return True
# APP1: recursion. TLE. Stack overflow
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        i, j = 0, len(s) - 1
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if i >= j:
            return True
        if i < j and s[i].lower() != s[j].lower():
            return False
        return self.isPalindrome(s[i + 1:j])
