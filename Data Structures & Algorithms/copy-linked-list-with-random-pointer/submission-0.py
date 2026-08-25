"""
import copy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# strategy:
# parse original through head
# store in hashmap as
# key = random pointer,
# value = node which need respective random pointer assigned
# when parsing also check self in hashmap, if self matches, then assign for all
# complexity: 3n, n for parse, n for self attach to map, n for assign all attached
# => O(n) time, O(n) space
# issue: node values aren't unique, how to hash?
# fix: parse through once to use hash table and establish relationship first, using counts for index
# then, you parse again, utilizing the relationship used. Still O(n)

from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        pointermap = defaultdict(list)
        countmap = defaultdict(list)

        dummy = Node(0)
        dummy.next = head
        cur_node = dummy
        count = 0

        while cur_node.next:
            cur_node = cur_node.next
            pointermap[cur_node.random].append(count)
            count += 1

        count = 0
        cur_node = dummy
        while cur_node.next:
            cur_node = cur_node.next
            while pointermap[cur_node]:
                to_reference = pointermap[cur_node].pop()
                countmap[count].append(to_reference)
            count += 1
        
        copy_list = [Node(0)] * (count)

        count = 0
        cur_node = dummy
        while cur_node.next:
            cur_node = cur_node.next
            copy_node = Node(cur_node.val)
            copy_list[count] = copy_node
            count += 1
        
        for i in range(len(copy_list)):
            if i < len(copy_list) - 1:
                copy_list[i].next = copy_list[i+1]
            while countmap[i]:
                to_connect_to = countmap[i].pop()
                copy_list[to_connect_to].random = copy_list[i]
        
        return copy_list[0]

        

            
