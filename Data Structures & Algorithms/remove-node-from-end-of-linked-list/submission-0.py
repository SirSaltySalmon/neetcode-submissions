# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        node_to_remove = length - n + 1
        count = 1
        cur_node = head
        prev_node = None
        while count < node_to_remove:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        
        # so now you want to remove cur_node.
        if prev_node is None:
            head = cur_node.next
        else:
            prev_node.next = cur_node.next
        
        return head

