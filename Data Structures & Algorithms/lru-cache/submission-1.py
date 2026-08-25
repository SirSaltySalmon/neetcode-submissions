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
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        # if key is in key_to_node, delete, then attach to tail
        # then fetch value and return
        # if not, return -1

        if key in self.key_to_node:
            node = self.key_to_node[key]

            if node != self.tail:
                # Remove node from current position
                if node.last:
                    node.last.next = node.next

                if node.next:
                    node.next.last = node.last

                if node == self.head:
                    self.head = node.next

                # Attach node to tail
                self.tail.next = node
                node.last = self.tail
                node.next = None
                self.tail = node

            return self.cache[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key is in key_to_node, delete, then attach to tail
        # if key is not in key_to_node,
        # 1. nothing in node, add as head
        # 2. something in node but not max capacity, add as tail
        # 3. max capacity, evict head
        #    eviction: delete from cache, list, AND key_to_node
        # then insert in cache

        if key in self.key_to_node:
            node = self.key_to_node[key]

            if node != self.tail:
                # Remove node from current position
                if node.last:
                    node.last.next = node.next

                if node.next:
                    node.next.last = node.last

                if node == self.head:
                    self.head = node.next

                # Attach node to tail
                self.tail.next = node
                node.last = self.tail
                node.next = None
                self.tail = node

        else:
            node = self.Node(key)

            if not self.head:
                self.head = node
                self.tail = node

            elif len(self.key_to_node) < self.capacity:
                self.tail.next = node
                node.last = self.tail
                self.tail = node

            else:
                # Evict least recently used node
                to_evict = self.head
                evict_key = to_evict.val

                new_head = self.head.next
                self.head = new_head

                if self.head:
                    self.head.last = None
                else:
                    self.tail = None

                del self.key_to_node[evict_key]
                del self.cache[evict_key]

                # Add the new node as most recently used
                if self.tail:
                    self.tail.next = node
                    node.last = self.tail
                    self.tail = node
                else:
                    # capacity == 1 case
                    self.head = node
                    self.tail = node

            self.key_to_node[key] = node

        # Insert/update value
        self.cache[key] = value