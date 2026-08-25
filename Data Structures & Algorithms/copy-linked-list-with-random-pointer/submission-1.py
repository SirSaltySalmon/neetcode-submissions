"""
import copy
import copy
import copy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}
        
        dummy = Node(0)
        dummy.next = head

        # first pass: create copies, and build references in hash
        cur_node = dummy
        prev_node = None
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
            copy_node = Node(cur_node.val)
            prev_copy_node = old_to_new.get(prev_node, Node(0))
            prev_copy_node.next = copy_node
            old_to_new[cur_node] = copy_node
        
        # second pass: attach randoms
        cur_node = dummy
        while cur_node.next:
            cur_node = cur_node.next
            copy_node = old_to_new[cur_node]
            copy_node.random = old_to_new[cur_node.random]
        
        return old_to_new[head]


        