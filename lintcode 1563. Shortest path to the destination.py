# APP1: BFS with hashmap, Time: O(nm) space; O(nm)
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param targetMap: 
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        if not targetMap or not targetMap[0]:
            return -1
        q = collections.deque([(0, 0)])
        dist = {(0, 0): 0}
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if targetMap[x][y] == 2:
                    return dist[(x, y)] 
                for dx, dy in DIRECTIONS:
                    _x, _y = x + dx, y + dy
                    # need to check _x, _y is valid
                    # if targetMap[_x][_y] == 2:
                    #     return dist[(x, y)] + 1
                    if self.is_valid(targetMap, _x, _y, dist):
                        q.append((_x, _y))
                        dist[(_x, _y)] = dist[(x, y)] + 1
        return -1
        
    def is_valid(self, targetMap, x, y, dist):
        if x < 0 or x >= len(targetMap) or y < 0 or y >= len(targetMap[0]):
            return False
        if targetMap[x][y] == 1:
            return False
        if (x, y) in dist:
            return False
        return True
