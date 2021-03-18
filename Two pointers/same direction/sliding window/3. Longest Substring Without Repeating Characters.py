class Solution:
    # APP1: find all substrings then check the uniqueness.
    # Time: O(n^3) space: O(n^2) Runtime: 64%

    # APP2: sliding deque + set. Time: O(n) space: O(n)
    # s = "abcabcbb"
    # q = [cb]
    # set = [bc]
        def lengthOfLongestSubstring(self, s: str) -> int:
            if not s:
                return 0
            max_len, right, n, q, uniq = 0, 0, len(s), collections.deque(), set()
            while right < n:
                if s[right] not in uniq:
                    uniq.add(s[right])
                else:
                    while s[q[0]] != s[right]:
                        ch = s[q.popleft()]
                        uniq.remove(ch)
                    q.popleft()
                q.append(right)
                right += 1
                max_len = max(max_len, right - q[0])
            return max_len

    #     APP3: two pointers + set. best
    #     Time: O(n) space: O(n) runtime: 90%
        def lengthOfLongestSubstring(self, s: str) -> int:
            if not s:
                return 0
            unique, n, left, right, res = set(), len(s), 0, 0, 0
            while right < n:
                if s[right] not in unique:
                    unique.add(s[right])
                    right += 1
                    continue
                res = max(res, len(unique))
                while s[left] != s[right]:
                    unique.remove(s[left])
                    left += 1
                left += 1
                right += 1
            res = max(res, len(unique))
            return res

    #     APP4: use dict data[ch] = idx. Runtime: 78%
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n, max_len, data, l = len(s), 0, {}, 0
        for idx, ch in enumerate(s):
            if ch in data:
                max_len = max(max_len, idx - l)
                # to get the correct l, need to see if the new ch and current l who's bigger so l won't got back. abba
                l = max(data[ch] + 1, l)
            # max_len = max(max_len, idx - l + 1)
            data[ch] = idx
        max_len = max(max_len, n - l)
        return max_len
