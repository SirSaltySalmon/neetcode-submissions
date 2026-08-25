# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        curNode = second_half
        prevNode = None
        while not curNode is None:
            temp = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = temp
        
        cur_node = head
        fast = prevNode
        while cur_node and fast:
            next_node = cur_node.next
            inserted_node = fast
            fast = fast.next
            cur_node.next = inserted_node
            inserted_node.next = next_node
            cur_node = next_node