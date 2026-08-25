# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target_node = head
        tail = head
        distance_left = n - 1
        while distance_left > 0:
            tail = tail.next
            distance_left -= 1
        
        prev_node = None
        while tail.next:
            prev_node = target_node
            target_node = target_node.next
            tail = tail.next
        
        if prev_node is None:
            head = target_node.next
        else:
            prev_node.next = target_node.next
        
        return head
            