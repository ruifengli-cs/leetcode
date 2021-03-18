class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        if not s or not k or k < 0:
            return 0
        res = left = 0
        n = len(s)
        char_cnt = {}
        for i in range(n):
            char_cnt[s[i]] = char_cnt.get(s[i], 0) + 1
            while len(char_cnt) >= k:
                res += n - i
                char_cnt[s[left]] -= 1
                if char_cnt[s[left]] == 0:
                    del char_cnt[s[left]]
                left += 1
        return res
