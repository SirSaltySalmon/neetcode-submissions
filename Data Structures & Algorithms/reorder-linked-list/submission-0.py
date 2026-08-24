# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # so its kinda like
        # go to end, insert node at end between nodes by decrementing
        if not head:
            return
        
        stack = [head]
        tail = head
        while tail.next:
            tail = tail.next
            stack.append(tail)
        
        cur_node = head
        # so now, you pop tail, and insert it between cur_node and cur_node.next
        while cur_node != stack[-1] and cur_node.next != stack[-1]:
            next_node = cur_node.next
            inserted_node = stack.pop()
            cur_node.next = inserted_node
            inserted_node.next = next_node
            cur_node = next_node
        
        stack.pop().next = None