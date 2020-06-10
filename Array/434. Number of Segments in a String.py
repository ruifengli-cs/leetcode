class Solution:
    # APP1: use split. Time: O(n) Space: O(n)
    def countSegments(self, s: str) -> int:
        return len(s.split())
    
    # APP2: one pass. Time: O(n) Space: O(1)
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        count = 1 if s[0] != ' ' else 0
        n = len(s)
        for i in range(1, n):
            if s[i - 1] == ' ' and s[i] != ' ':
                count += 1
        return count
