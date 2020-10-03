# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # APP1: add parent link, then do BFS
    # Time: O(n) Space: O(n)
    #     def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    #         if not root or not target or K < 0:
    #             return []
    #         parents = {root: None}
    #         self.build_parent(root, parents)
    #         q, res, dist = collections.deque([(target)]), [], {target: 0}
    #         while q:
    #             node = q.popleft()
    #             if node:
    #                 if dist[node] == K:
    #                     res.append(node.val)
    #                     continue
    #                 if node.left and node.left not in dist:
    #                     q.append(node.left)
    #                     dist[node.left] = dist[node] + 1
    #                 if node.right and node.right not in dist:
    #                     q.append(node.right)
    #                     dist[node.right] = dist[node] + 1
    #                 if parents[node] and parents[node] not in dist:
    #                     q.append(parents[node])
    #                     dist[parents[node]] = dist[node] + 1
    #         return res

    #     def build_parent(self, root, parents):
    #         if not root:
    #             return
    #         if root.left:
    #             parents[root.left] = root
    #             self.build_parent(root.left, parents)
    #         if root.right:
    #             parents[root.right] = root
    #             self.build_parent(root.right, parents)

    # APP1: refacter code:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root or not target or K < 0:
            return []
        self.add_parent(root)
        q, res, visited = collections.deque([(target, 0)]), [], set([target])
        while q:
            node, dis = q.popleft()
            if dis == K:
                res.append(node.val)
            for nei in (node.parent, node.left, node.right):
                if nei and nei not in visited:
                    q.append((nei, dis + 1))
                    visited.add(nei)
        return res

    def add_parent(self, node, parent=None) -> None:
        if not node:
            return
        node.parent = parent
        self.add_parent(node.left, node)
        self.add_parent(node.right, node)
















