# APP1: two pointers + dict to store the count of the char frequence.
# Time: O(n) space: O(n) Runtime: 60
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k <= 0:
            return 0
        count, n, left, res = {}, len(s), 0, 0
        for i in range(n):
            while left <= i and s[i] not in count and len(count) >= k:
                count[s[left]] -= 1
                if not count[s[left]]:
                    del count[s[left]]
                left += 1

            count[s[i]] = count.get(s[i], 0) + 1
            res = max(res, i - left + 1)
        return res
