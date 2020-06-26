class Solution:
    # APP1: brute force Time: O(n^2) Space: O(1), Runtime: TLE
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n, max_area = len(heights), 0
        for i in range(n):
            min_h = sys.maxsize
            for j in range(i, n):
                min_h = min(min_h, heights[j])
                area = (j - i + 1) * min_h
                max_area = max(max_area, area)
        return max_area
    
    # APP2: for each h, need to it's left most and right most boundry to get area.
    # time: O(n ^ 2) space: O(1), Runtime: TLE
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n, max_area = len(heights), 0
        for i in range(n):
            area = self.find_area(heights, i)
            max_area = max(max_area, area)
        return max_area
        
    def find_area(self, heights, i):
        l = r = i
        while l - 1 >= 0 and heights[l - 1] >= heights[i]:
            l -= 1
        while r + 1 < len(heights) and heights[r + 1] >= heights[i]:
            r += 1
        return (r - l + 1) * heights[i]
        
    # APP3: for each h, need to know it's first left lower and first right lower in O(1). 
    # use a increasing monotone stack, for new h, pop all item >= h to find first left lower
    # can't find first right lower until it's been popped out. 
    # So we can calculate the area when popping out each item. add -1 to the end to pop out all items.
    # Time: O(n), Space: O(n) Runtime: 100ms 96%
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n, max_area, stack = len(heights), 0, []
        for i, val in enumerate(heights + [-1]):
            while stack and heights[stack[-1]] >= val:
                idx = stack.pop()
                left_index = stack[-1] if stack else -1
                max_area = max(max_area, heights[idx] * (i - left_index - 1))
            stack.append(i)
        return max_area
        
