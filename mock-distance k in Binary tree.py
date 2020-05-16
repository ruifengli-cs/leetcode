# 1506. All Nodes Distance K in Binary Tree
# We are given a binary tree (with root node root), a target node, and an integer value K.

# Return a list of the values of all nodes that have a distance K from the target node. The answer can be returned in any order.


#      1
#     /  \
#    2   3
#   / \   \
# 4    5  6

# target: 1          2     4
# k:      2          2     1
#       [4,5,6]      3     2
        

# down: left, right
# up: distance from root to node
# hashmap1: key: distance from node to root, value; list of nodes
# 0: [1]
# 1: [2, 3]
# 2: [4, 5, 6]
# hashmap2: key: node value: distance from node to root

#             1. node.left/ 2. node.right/ 3. node.parent
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import collections
class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    """
    def distanceK(self, root, target, K):
        # parent: node: parent_node
        parent = {root: None}
        self.add_parent(root, parent)
        q = collections.deque([target])
        visited = set([target])
        res = []
        
        distance = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if distance == K:
                    res.append(node.val)
                    continue
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                node_parent = parent[node]
                if node_parent and node_parent not in visited:
                    q.append(node_parent)
                    visited.add(node_parent)
            distance += 1
        return res
    
    def add_parent(self, root, parent):
        if not root:
            return
        if root.left:
            parent[root.left] = root
            self.add_parent(root.left, parent)
        if root.right:
            parent[root.right] = root
            self.add_parent(root.right, parent)
        

input:  
[3,5,1,6,2,0,8,null,null,7,4]
5
2

expect: 
[7,4,1]

output: 

[[7],[4],[1,0,8]]

        
        
        3
     5     1
6      2 0    8
     7  4
        
        
feedback: 
1. need to clarify the output         
2. bug: should start from target
3. flat out the tree using parent and bfs.
4. if dfs doesn't work, try bfs on tree.
