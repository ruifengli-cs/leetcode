class Solution:
    # APP1: use set store ch: index pair. use two pointers to find max unique strings.
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        uniq_chars, l = set(), 0
        max_len = 0
        for r, ch in enumerate(s):
            if ch in uniq_chars:
                max_len = max(max_len, r - l)
            while ch in uniq_chars:
                uniq_chars.remove(s[l])
                l += 1
            uniq_chars.add(ch)
        max_len = max(max_len, r - l + 1)
        return max_len

    # APP2: use hashmap to store ch, no need to delete ch
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n, max_len, l = len(s), 0, 0
        uniq_chars = {}
        for r, ch in enumerate(s):
            if ch in uniq_chars:
                # to get the correct l, need to see if the new ch and current l who's bigger so l won't got back.
                l = max(uniq_chars[ch] + 1, l)
            max_len = max(max_len, r - l + 1)
            uniq_chars[ch] = r
        return max_len