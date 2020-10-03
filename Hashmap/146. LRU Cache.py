# APP1: use OrderedDict. Time: O(1), Space: O(n)
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1:
            self.cache.move_to_end(key, last=False)
        return val

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
        if len(self.cache) > self.capacity:
            self.cache.popitem()

        # APP2: dict + doublly linkedlist. Time: O(1) Space: O(n)


class DoublyLinkedNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DoublyLinkedNode(-1, -1)
        self.tail = DoublyLinkedNode(-1, -1)
        self.head.next, self.tail.pre = self.tail, self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.move_to_front(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
        else:
            self.cache[key] = DoublyLinkedNode(key, value)
            if len(self.cache) > self.capacity:
                self.popitem()
        self.move_to_front(key)

    def move_to_front(self, key: int) -> None:
        node = self.cache[key]
        # dettach cur node
        if node.pre and node.next:
            node.pre.next, node.next.pre = node.next, node.pre
        # insert cur node to front
        node.pre, node.next = self.head, self.head.next
        node.next.pre, self.head.next = node, node

    def popitem(self) -> None:
        del self.cache[self.tail.pre.key]
        node = self.tail.pre.pre
        node.next, self.tail.pre = self.tail, node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)