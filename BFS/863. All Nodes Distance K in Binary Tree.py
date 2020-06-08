# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
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