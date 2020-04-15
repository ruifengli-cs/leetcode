class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
# APP1: loop list, use two pointers in same directions
# Time: O(n^2) Space: O(1). Runtime: Memory: 
    def minimumBoxes(self, boxes, target):
        # write your code here
        if not boxes or target < 0:
            return -1
        ans = sys.maxsize
        for i in range(1, len(boxes)):
            left_min = self.find_min(boxes, target, 0, i)
            right_min = self.find_min(boxes, target, i, len(boxes))
            if left_min != sys.maxsize and right_min != sys.maxsize:
                ans = min(ans, left_min + right_min)
        if ans == sys.maxsize:
            return -1
        return ans
    
    def find_min(self, boxes, target, start, end):
        slow = start
        now_sum = 0
        length = sys.maxsize
        for fast in range(start, end):
            now_sum += boxes[fast]
            while now_sum > target:
                now_sum -= boxes[slow]
                slow += 1 
            if now_sum == target:
                length = min(length, fast - slow + 1)
        return length
        
# APP2: preprocessing 
# Time: O(n), space: O(n)
    def minimumBoxes(self, boxes, target):
        # write your code here
        if not boxes or target < 0:
            return -1
        left_min = self.find_min(boxes, target)
        reversed_box = boxes[::-1]
        right_min = self.find_min(reversed_box, target)
        right_min = right_min[::-1]
        ans = sys.maxsize
        for i in range(len(boxes) - 1):
            if left_min[i] != sys.maxsize and right_min[i + 1] != sys.maxsize:
                ans = min(ans, left_min[i] + right_min[i + 1])
        if ans == sys.maxsize:
            return -1
        return ans

    def find_min(self, boxes, target):
        slow = now_sum = 0
        res = []
        length = sys.maxsize
        for fast in range(len(boxes)):
            now_sum += boxes[fast]
            while now_sum > target:
                now_sum -= boxes[slow]
                slow += 1 
            if now_sum == target:
                length = min(length, fast - slow + 1)
            res.append(length)
        return res 
