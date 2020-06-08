# Note
1. Python map() function

map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
eg. LeetCode 66. Plus One
Input: [1,2,3]
Output: [1,2,4]
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))
        
