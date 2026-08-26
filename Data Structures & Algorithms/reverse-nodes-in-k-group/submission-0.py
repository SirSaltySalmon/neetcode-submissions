# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 1:
            return head
        
        true_head = None
        cur_head = head
        cur_tail = None

        while True:
            headpointer = cur_head
            tailpointer = cur_head
            for i in range(k-1):
                tailpointer = tailpointer.next
                if tailpointer is None:
                    # connect cycle start to last cycle
                    cur_tail.next = headpointer
                    return true_head
            next_cycle_head = tailpointer.next
            
            # now contained between headpointer and tailpointer are
            # nodes we should reverse
            cur_node = headpointer
            prev_node = None
            while prev_node != tailpointer:
                temp = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = temp
            
            if true_head is None:
                true_head = tailpointer
            else:
                cur_tail.next = tailpointer
            cur_tail = headpointer

            if next_cycle_head is None:
                return true_head
            cur_head = next_cycle_head
        
        return true_head


