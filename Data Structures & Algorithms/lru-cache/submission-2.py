class LRUCache:
    class Node:
        def __init__(self, val, next=None, last=None):
            self.val = val
            self.next = next
            self.last = last

    capacity: int
    cache: dict
    key_to_node: dict
    head: Node
    tail: Node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.key_to_node = {}
        self.head = self.Node(0)
        self.tail = self.Node(0)
        self.head.next = self.tail
        self.tail.last = self.head
    
    def _remove(self, node):
        lst, nxt = node.last, node.next
        lst.next, nxt.last = nxt, lst

    def _add_to_end(self, node):
        prev = self.tail.last
        prev.next = node
        node.last = prev
        node.next = self.tail
        self.tail.last = node

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove(node)
            self._add_to_end(node)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove(node)
            self._add_to_end(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                to_evict = self.head.next
                evict_key = to_evict.val
                self._remove(to_evict)
                del self.key_to_node[evict_key]
                del self.cache[evict_key]
            
            node = self.Node(key)
            self._add_to_end(node)
            self.key_to_node[key] = node

        self.cache[key] = value