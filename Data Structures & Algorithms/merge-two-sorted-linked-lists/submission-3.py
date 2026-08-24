# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur_node = dummy
        while list1 and list2:
            next_node = None
            #get the smaller out of the two
            if list1.val < list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next
            
            cur_node.next = next_node
            cur_node = cur_node.next
        
        # attach remaining nodes
        while list1:
            cur_node.next = list1
            cur_node = cur_node.next
            list1 = list1.next
        
        while list2:
            cur_node.next = list2
            cur_node = cur_node.next
            list2 = list2.next
        
        return dummy.next
            
