# APP1: brute force. find all substrings of s. if Counter(sub) & Counter(t) == Counter(t), then track the start and end.
# Time: O(n^2) space:O(n^2)

# APP2: use count_t, count_s store ch:freq mapping. use count to store how manu char has been correctly presented in t.
# use two pointers to document count_s
# Time: O(n) space: O(n) Runtime: 82%

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        t_map = Counter(t)
        s_map = {}
        n = len(s)
        max_len = n + 1
        left = count = 0
        start, end = 0, n
        for i in range(n):
            ch = s[i]
            if ch not in t_map:
                continue
            s_map[ch] = s_map.get(ch, 0) + 1
            if s_map[ch] == t_map[ch]:
                count += 1
            while count == len(t_map):
                if i - left + 1 < max_len:
                    max_len = i - left + 1
                    start, end = left, i
                if s[left] in s_map:
                    s_map[s[left]] -= 1
                    if s_map[s[left]] < t_map[s[left]]:
                        count -= 1
                left += 1

        return s[start:end + 1] if end != n else ""
