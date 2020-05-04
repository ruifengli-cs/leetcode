# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # # # dfs, pre-order traverse
    # # serialize: O(n)  Space: O(n) runtime: 84% memory: 24%
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "# "
        return self.pre_order(root, "")

    def pre_order(self, root, string):
        if not root:
            return string + "# "

        string += str(root.val) + " "
        string = self.pre_order(root.left, string)
        string = self.pre_order(root.right, string)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        q = collections.deque(data.split(' '))
        return self.dfs(q)

    def dfs(self, q):
        if q and q[0] == '#':
            q.popleft()
            return None
        node = q[0]
        q.popleft()
        root = TreeNode(node)
        root.left = self.dfs(q)
        root.right = self.dfs(q)
        return root

    # # APP2 iteration using stack to minic dfs, pre-order traverse
    # note that add right to the stack first
    # serialize: O(n)  Space: O(n) Runtime: 73 memory: 24%
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        stack = [root]
        res = ""
        while stack:
            node = stack.pop()
            if not node:
                res += "# "
                continue
            res += str(node.val) + ' '
            stack.append(node.right)
            stack.append(node.left)
        return res

    #     use checked_child_cnt to count how many childer has been checked. if 0 then form left, if 1 form right
    # also need to add the parent back to stack if count < 1
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(' ')
        root = TreeNode(data[0]) if data[0] != '#' else None
        stack = [(root, 0)]
        i = 1
        while stack and i < len(data):
            node, checked_child_cnt = stack.pop()
            new_node = TreeNode(data[i]) if data[i] != '#' else None

            if checked_child_cnt == 0:
                node.left = new_node
                checked_child_cnt += 1
                stack.append((node, checked_child_cnt))
            elif checked_child_cnt == 1:
                node.right = new_node
            if new_node:
                stack.append((new_node, 0))
            i += 1
        return root

    # APP3 bfs. layer by layer
    # serialize time: O(n) space: O(n) Runtime: 98% memory: 24%
    def serialize(self, root):
        if not root:
            return "#"
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node is None:
                res.append("#")
                continue
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ' '.join(res)

    # deserialize, form nodes first, then use two pointers to connect nodes
    # time: O(n) space: O(n)
    def deserialize(self, data):
        data = data.split(' ')
        nodes = [TreeNode(item) if item != '#' else None for item in data]
        slow, fast, root = 0, 1, nodes[0]
        while fast < len(data):
            if nodes[slow] is None:
                slow += 1
                continue
            nodes[slow].left = nodes[fast]
            fast += 1
            nodes[slow].right = nodes[fast]
            fast += 1
            slow += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))