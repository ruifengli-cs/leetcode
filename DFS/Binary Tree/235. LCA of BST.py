# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # APP1: dfs: return LCA.
    # case1: cur = p or q, return cur
    # case2: both p, q on left or right, then return left or right
    # case3: none of p, q on left or right. or cur is None, return None
    # case4: p, q on left or right each, return root
    # assumption is both p, q are in BST
    # Time: O(n) space: O(n) stack worst case. Runtime: 6%
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root or not p or not q:
                return None
            return self.dfs(root, p, q)

        def dfs(self, root, p, q):
            if not root or root == p or root == q:
                return root
            left = self.dfs(root.left, p, q)
            right = self.dfs(root.right, p, q)
            if left and right:
                return root
            if left or right:
                return left or right
            return None

    # APP2: since it's BST, we can compare root.val with p.val, q.val.
    # if both less than root.val, dfs root.left. if both larger, dfs root.right. Otherwise return root
    # Time: O(n) Space: O(n) Runtime: 68%
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
    #         return root

    # APP3: iteration. Runtime: 85%
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root or not p or not q:
                return None
            cur = root
            while cur:
                if q.val < cur.val and p.val < cur.val:
                    cur = cur.left
                elif q.val > cur.val and p.val > cur.val:
                    cur = cur.right
                else:
                    return cur

    #     APP4: based on APP3. one liner. Runtime: 85%
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root