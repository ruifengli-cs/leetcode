
class Solution:
    def delete_nodes(self, root, to_delete):
        if not root:
            return []
        if not to_delete:
            return [root]
        data, roots = self.get_data(root), set([root])

        for num in to_delete:
            node, parent, side = data[num]
            if node in roots:
                roots.remove(node)
            # add it's children to roots
            if node.left:
                roots.add(node.left)
            if node.right:
                roots.add(node.right)
            # remove the node from the tree
            self.remove_node(data, num)
        return list(roots)

    def remove_node(self, data, num):
        node, parent, side = data[num]
        if parent:
            if side == "left":
                parent.left = None
            else:
                parent.right = None
        if node.left:
            data[node.left.val] = node.left, None, None
        if node.right:
            data[node.right.val] = node.right, None, None
        node.left = None
        node.right = None

    def get_data(self, root):
        data = {}
        self.dfs(root, data, None, None)
        return data

    def dfs(self, root, data, parent, side):
        if not root:
            return
        data[root.val] = root, parent, side
        self.dfs(root.left, data, root, "left")
        self.dfs(root.right, data, root, "right")


https: // leetcode.com / problems / delete - nodes - and -
return -forest / submissions /

Definition
for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


从下向上


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        self.delete = set(to_delete)
        self.dfs(root, None)
        return self.res

    def dfs(self, root, parent):
        if not root:
            return
        self.dfs(root.left, root)
        self.dfs(root.right, root)

        if root.left and root.left.val in self.delete:
            root.left = None
        if root.right and root.right.val in self.delete:
            root.right = None

        if (not parent or parent.val in self.delete) and root.val not in self.delete:
            self.res.append(root)
        elif root.val in self.delete:
            root.left = None
            root.right = None


从上向下


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.res = []
        delete = set(to_delete)
        self.dfs(root, True, delete)
        return self.res

    def dfs(self, root, is_root, delete):
        if not root:
            return None
        root_delete = root.val in delete
        if is_root and not root_delete:
            self.res.append(root)
        root.left = self.dfs(root.left, root_delete, delete)
        root.right = self.dfs(root.right, root_delete, delete)
        return root if not root_delete else None

        # APP1: dfs: 1. return root after the deletion.
        # 2. if cur is in to_delete, ignore
        # 3. if cur.child in to_delete, remove child link
        def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
            if not root or not to_delete:
                return root
            to_delete, res = set(to_delete), []
            self.dfs(root, to_delete, res, True)
            return res

        def dfs(self, root, to_delete, res, is_new_root):
            if not root:
                return
            if is_new_root and root.val not in to_delete:
                res.append(root)
            delete_cur_root = True if root.val in to_delete else False
            root.left = self.dfs(root.left, to_delete, res, delete_cur_root)
            root.right = self.dfs(root.right, to_delete, res, delete_cur_root)
            return None if delete_cur_root else root