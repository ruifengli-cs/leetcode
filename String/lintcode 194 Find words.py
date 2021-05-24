class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """

    # n = len(str), m = len(dict) k: average word length in dict
    # cannot use trie since trie is more used for substring
    # follow up: if n is really larget, n = 10 ** 6

    # APP1: brute force. for each word in dict, find if there's a subsequense in string using two pointers
    # Time: O(nm) space: O(1)
    def findWords(self, str, dict):
        if not str:
            return []
        res = []
        for word in dict:
            cur_word = cur_str = 0
            while cur_str < len(str) and cur_word < len(word):
                if str[cur_str] != word[cur_word]:
                    cur_str += 1
                    continue
                cur_word += 1
                cur_str += 1
            if cur_word == len(word):
                res.append(word)
        return res

    # APP2: brute force. find all subsequese in string using dfs, check if it's in dict
    # Time: O(2^n * m) space: O(1) Runtime: TLE
    def findWords(self, str, dict):
        if not str or not dict:
            return []
        subsqs = set()
        self.get_subsqs(str, subsqs, 0, "")
        res = []
        for subsq in subsqs:
            if subsq in dict:
                res.append(subsq)
        return res

    def get_subsqs(self, str, subsqs, idx, sub):
        if idx >= len(str):
            return

        new_sub = sub + str[idx]
        subsqs.add(new_sub)
        self.get_subsqs(str, subsqs, idx + 1, new_sub)
        self.get_subsqs(str, subsqs, idx + 1, sub)
        return

    # APP3: opt APP1 using hashmap: for each char, store it's indexes.
    # str="bcokdok" b: [0], c:[1], o:[2,5], k:[3,6], d:[4]
    # Time: O(m * k * lgn) space: O(n)
    def findWords(self, str, dict):
        if not str or not dict:
            return []
        mapping = collections.defaultdict(list)
        res = []
        for i in range(len(str)):
            mapping[str[i]].append(i)
        for word in dict:
            cur_str = cur_word = 0
            for char in word:

                if char not in mapping:
                    break
                pos = self.binary_search(mapping[char], char, cur_str)
                if pos == -1:
                    break
                cur_word += 1
                cur_str = pos + 1
            if cur_word == len(word):
                res.append(word)
        return res

    def binary_search(self, array, char, target_start):
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] < target_start:
                start = mid
            else:
                end = mid
        if array[start] >= target_start:
            return array[start]
        if array[end] >= target_start:
            return array[end]
        return -1

    # APP4: opt APP1 by preprocess the string, use 2D array to store for every index, where it's next char index will be.
    # eg. mapping[0][0] = 5, mapping[1][2]=2 for str="bcogtadsjofisdhklasdj"
    # Time: O(mk) space: O(n * 26)

    def findWords(self, str, dict):
        if not str or not dict:
            return []
        data, n, res = self.get_data(str), len(str), []
        for word in dict:
            idx = cur_word = 0
            while cur_word < len(word):
                ch = word[cur_word]
                pos = data[idx][ord(ch) - ord('a')]
                if pos == n:
                    break
                idx = pos + 1
                cur_word += 1
            if cur_word == len(word):
                res.append(word)
        return res

    def get_data(self, s):
        n = len(s)
        data = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                data[i][j] = i if ord(s[i]) - ord('a') == j else data[i + 1][j]
        return data
