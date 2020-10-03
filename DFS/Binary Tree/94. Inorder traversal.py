# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # APP1: DFS. Time: O(n) space: stack O(lgn) Runtime: 94%
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root: TreeNode, res: List[int]):
        if not root:
            return
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)

    # APP2: stack
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, cur, stack = [], root, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res

    # APP3: stack + dummy node
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        dummy = TreeNode(-1)
        dummy.right = root
        res, stack = [], [dummy]
        while stack:
            cur = stack.pop()
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                res.append(stack[-1].val)
        return res





