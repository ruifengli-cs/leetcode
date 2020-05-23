# Please judge whether there is a cycle in the directed graph with n vertices and m edges. The parameter is two int arrays. There is a directed edge from start[i] to end[i].

# 1. 
# Input: start = [1],end = [2]
# Output: "False"
# Explanation:
# There is only one edge 1->2, and do not form a cycle.


# 2. 
# Input: start = [1,2,3],end = [2,3,1]
# Output: "True"
# Explanation:
# There is a cycle 1->2->3->1.
# 1:[2]
# 2:[3]
# 3:[1]
    
# q: 1| 2  |3     | 1
# v: 1| 1,2 |1,2,3| 
# visited to store visted vertices.


# start = [1,2,2],end = [2,3,1]

#   4-1-2
#     |
#     3
# 1: brute force: 
# 1:[2,3,4]

    
    
# 3 <- 1 -> 2 -> 3
# indegree:
# 1: 0
# 2: 1
# 3: 2

# 1 -> 2 -> 3 -> 1
# indegree:
# 1: 1
# 2: 1
# 3: 2
    
1 -> 2 -> 3 -> 2
^         |
----------

1-2-3-1
1-2-3-2-3-2-3-2


indegree:
1: 0 |  
2: 2 | 1
3: 1 | 1
begin = 1
output = [1,2,3,1]
begin = 2
output = [2,3,2]
begin = 3
output = [3,2,3]

begin: any node in the graph
    
case:
1 -> 2 -> 3 -> 2
begin: 1
1-2-3-2
     
# topological sort: indegree. if still has and all the current ingree not 0 then has circle.
import collections
class Solution:
    def find_cycle(self, start, end):
        if not start or not end:
            return False
        data = collections.defaultdict(list)
        indegree = {}
        n = len(start)
        for i in range(n):
            indegree[end[i]] = indegree.get(indegree[end[i]], 0) + 1
            data[start[i]].append(end[i])
        
        q = collections.deque()
        for key, val in indegree.items():
            if val == 0:
                q.append(key)
                        
        while q:
            node = q.popleft()
            neighbour = data[node]
            for nb in neighbour:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        
        for key, val in indegree.items():
            if val != 0:
                return False
        return True
    
    def print_cycle(self, start, end, begin):
        if not start or not end or begin is None:
            return []
        data = collections.defaultdict(list)
        
        n = len(start)
        for i in range(n):
            data[start[i]].append(end[i])
        path = []
        visited = set()
        paths = self.dfs(data, path, 0, visited, begin)
        if not paths:
            return []
        path_dict = {}
        min_len = len(paths[0])
        for path in paths:
            min_len = min(min_len, len(path))
            path_dict[len(path)] = path
        return path_dict[min_len]
            
        self.res = []
        
    #defination: return the all the paths for the cycle
    def dfs(self, data, path, length, visited, begin):
        
        
        
https://www.lintcode.com/problem/directed-graph-loop/description
    
    
    
    
    
    
    
