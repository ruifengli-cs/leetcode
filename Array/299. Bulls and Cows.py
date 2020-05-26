class Solution:
    # APP1: loop through guess, first pass to find bulls, second pass to find cows
    def getHint(self, secret: str, guess: str) -> str:
        if not secret or not guess:
            return ""
        mapping = {}
        n, m = len(secret), len(guess)
        bulls = cows = 0
        # first pass to find bulls
        for i in range(n):
            if guess[i] == secret[i]:
                bulls += 1
                continue
            mapping[secret[i]] = mapping.get(secret[i], 0) + 1

        # second pass to find cows
        for i in range(n):
            if guess[i] == secret[i] or guess[i] not in mapping:
                continue
            cows += 1
            mapping[guess[i]] -= 1
            if mapping[guess[i]] == 0:
                del mapping[guess[i]]

        return str(bulls) + 'A' + str(cows) + 'B'

    # APP2: one pass, maintain an array of length 10. if ch in secret, then array[ch]++, if ch in guess, array[ch]--.
    # add cow if array[ord(ch) - ord('0')] < 0
    def getHint(self, secret: str, guess: str) -> str:
        if not secret or not guess:
            return ""
        visited = [0] * 10
        n = len(secret)
        bulls = cows = 0
        for i in range(n):
            s, g = secret[i], guess[i]
            if s == g:
                bulls += 1
            else:
                if visited[int(s)] < 0:
                    cows += 1

                if visited[int(g)] > 0:
                    cows += 1
                visited[int(s)] += 1
                visited[int(g)] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
