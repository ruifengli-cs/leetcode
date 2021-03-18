# code a lru wrapper to call the function
# 3-1-2-4-5
class ListNode:
    def __init__(self, key, val):
        self.pre = None
        self.next = None
        self.val = val
        self.key = key

class LRU_cache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.capacity = capacity
        self.head.next, self.tail.pre = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_front(key)
            return self.cache[key].val
        new_val = black_box_get_val(key)
        self.put(key, new_val)
        return new_val

    def put(self, key: int, value: int) -> None:
        self.cache[key] = ListNode(key, value)
        if len(self.cache) >= self.capacity:
            self.pop_item()
        self.move_to_front(key)

    def move_to_front(self, key: int) -> None:
        node = self.cache[key]
        if node.pre and node.next:
            node.pre.next, node.next.pre = node.next, node.pre

        node.pre, node.next = self.head, self.head.next
        self.head.next, node.next.pre = node, node

    def pop_item(self):
