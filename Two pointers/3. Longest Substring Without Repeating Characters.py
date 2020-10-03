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

    #     APP3: two pointers + set
    #     Time: O(n) space: O(n) runtime: 71%
        def lengthOfLongestSubstring(self, s: str) -> int:
            if not s:
                return 0
            n, l, r, uniq, max_len = len(s), 0, 0, set(), 0
            while r < n:
                if s[r] in uniq:
                    max_len = max(max_len, r - l)
                while s[r] in uniq:
                    uniq.remove(s[l])
                    l += 1
                uniq.add(s[r])
                r += 1
            max_len = max(max_len, r - l)
            return max_len

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
