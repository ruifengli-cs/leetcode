# APP1: brute force. get all substring, calculate each sub for each char.
# TIme: O(n^2) space: O(unique char in s)

# APP2: sliding window + dict
# if m is the unique char in window, then we can try 26 times sliding window.
# Time: O(26n) space: O(26n) Runtime: 21%
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or not k or k <= 0:
            return 0
        res = 0
        for m in range(1, 27):
            res = max(res, self.helper(s, k, m))
        return res

    def helper(self, s, k, m):
        uniq, n = {}, len(s)
        res, right, count = 0, 0, 0
        for i in range(n):
            # uniq[s[i]] = uniq.get(s[i], 0) + 1
            while right < n and len(uniq) <= m:
                uniq[s[right]] = uniq.get(s[right], 0) + 1
                if uniq[s[right]] == k:
                    count += 1

                if len(uniq) == m and count == m:
                    res = max(res, right - i + 1)
                right += 1
            uniq[s[i]] -= 1
            if uniq[s[i]] == k - 1:
                count -= 1
            if uniq[s[i]] == 0:
                del uniq[s[i]]
        return res