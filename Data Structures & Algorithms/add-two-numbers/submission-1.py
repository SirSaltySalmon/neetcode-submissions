# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        cur_node = head
        while l1 and l2:
            result = l1.val + l2.val + carry
            digit = result % 10
            carry = result // 10
            cur_node.val = digit
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                cur_node.next = ListNode(0)
                cur_node = cur_node.next
        
        while l1:
            result = l1.val + carry
            digit = result % 10
            carry = result // 10
            cur_node.val = digit
            l1 = l1.next
            if l1:
                cur_node.next = ListNode(0)
                cur_node = cur_node.next
            else:
                cur_node.next = None
        
        while l2:
            result = l2.val + carry
            digit = result % 10
            carry = result // 10
            cur_node.val = digit
            l2 = l2.next
            if l2:
                cur_node.next = ListNode(0)
                cur_node = cur_node.next
            else:
                cur_node.next = None
        
        if carry != 0:
            cur_node.next = ListNode(carry)

        return head
        
