1. For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


        
(1) n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 
    
Output: [1]

    
# find the node which has shortest path to all leaf nodes
 0 - 1 - 2

(2) n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

0-1-2-3-4-5-6-7

hashmap: connect_degree 0:1, 1:1, 3:4


        
Output: [3, 4]
    
1, use defaultdict: 3: [0,1,2,4] to re-store the data
2, traverse all the nodes, for each node, do bfs and count it's longest path
3, use hashmap to store node: longest path
3. find the shortest logest path and append the nodes
# Time: O(V*E) space: O(V + E) V:node E: edge
        
class Solution:
    def find_mhts(self, n, edges):
        if not n or n < 0:
            return []
        data = collections.defaultdict(list)
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            data[node1].append(node2)
            data[node2].append(node1)
        mapping = collections.defaultdict(list)
        for i in range(n):
            longest_path = self.bfs(i, data)
            mapping[longest_path].append(i)
        candidate = sys.maxsize
        for key, val in mapping.items():
            candidate = min(key, candidate)
        if candidate == sys.maxsize:
            return []
        return mapping[candidate]
    
    def bfs(self, i, data):
        q = collections.deque([i])
        path_length = -1
        visited = set([i])
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node in data:
                    for d in data[node]:
                        if d not in visited:
                            q.append(d)
                            visited.add(d)
            path_length += 1
        return path_length
    
lession: 
    1. undirectional graph can also use topological sorting.
    2. in bfs, use tuple to simplify nested for loop.
    
    
https://leetcode.com/problems/minimum-height-trees/
