class Solution:
    # APP1: counter to get most freq, then output
    # Time: O(n + klgk) where n = len(s), k = len(set(s)) Space: O(n)
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        res, count = [], collections.Counter(s)
        for cha, freq in count.most_common():
            res.append(cha * freq)
        return ''.join(res)

    #     APP2: bucket sort by frequency.
    #     Time: O(n) Space: O(n)
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        count = collections.Counter(s)
        max_freq = max(count.values())
        buckets, res = collections.defaultdict(list), []
        for ch, freq in count.items():
            buckets[freq].append(ch)
        for i in range(max_freq, 0, -1):
            if i not in buckets:
                continue
            for char in buckets[i]:
                res.append(char * i)
        return ''.join(res)



