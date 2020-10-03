class Solution:
    # APP1: use counter then sort counter.
    # Time: O(n + klgk) space: O(n) where n = len(s), k = len(set(s)) Runtime: 97%
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        res, count = [], collections.Counter(s)
        for key, val in count.most_common():
            res.append(key * val)
        return "".join(res)

    # APP2: use counter and bucket sort - defaultdict key: frequency, val:
    # time: O(n) space: O(n) Runtime: 49%
    def frequencySort(sefl, s: str) -> str:
        if not s:
            return ""
        res, count, bucket = [], collections.Counter(s), collections.defaultdict(list)
        for ch, freq in count.items():
            bucket[freq].append(ch)
        max_frequency = max(count.values())

        for i in range(max_frequency + 1, 0, -1):
            for ch in bucket[i]:
                res.append(i * ch)
        return ''.join(res)