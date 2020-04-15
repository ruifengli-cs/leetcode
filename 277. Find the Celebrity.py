# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
# APP1: brute force 1, nested for loop with hashmap, 3 pass
# Runtime: TLE
    def findCelebrity(self, n: int) -> int:
        if not n or n < 0:
            return -1
        mapping = {}
        for i in range(n):
            mapping[i] = True
        for i in range(n - 1):
            for j in range(i + 1, n):
                if knows(i, j):
                    mapping[i] = False
                else:
                    mapping[j] = False
                if knows(j, i):
                    mapping[j] = False
                else:
                    mapping[i] = False
        for ppl, is_celeb in mapping.items():
            if is_celeb:
                return ppl
        return -1
    
# APP2: brute force 2, loop through ppl list and check celebrity
# Time: O(n^2) space: O(1) Runtime: 23%  memory: 100
    def findCelebrity(self, n: int) -> int:
        if not n or n < 0:
            return -1
        for i in range(n):
            if self.is_celeb(i, n):
                return i
        return -1
    
    def is_celeb(self, candidate, n):
        for i in range(n):
            if candidate == i:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return False
        return True

# APP3: two pass, first find candidate, then check throughly
# Time: O(n), space: O(1) runtime: 81%  memory: 100
    def findCelebrity(self, n: int) -> int:
        if not n or n < 0:
            return -1 
        candi = 0
        for i in range(1, n):
            if knows(candi, i):
                candi = i
        for i in range(n):
            if candi == i:
                continue
            if knows(candi, i) or not knows(i, candi):
                return -1
        return candi
        
# APP4: if api is expensive, two pass like APP3, store first pass in hashmap
# Time: O(n), space: O(n) runtime: 81%  memory: 100
    def findCelebrity(self, n: int) -> int:
        if not n or n < 0:
            return -1 
        mapping = {}
        candi = 0
        for i in range(1, n):
            if knows(candi, i):
                mapping[(candi, i)] = True
                candi = i
            else:
                mapping[(candi, i)] = False
        for i in range(n):
            if candi == i:
                continue
            if (candi, i) in mapping and mapping[(candi, i)]:
                return -1
            if (i, candi) in mapping and not mapping[(i, candi)]:
                return -1
            if knows(candi, i) or not knows(i, candi):
                return -1
        return candi
